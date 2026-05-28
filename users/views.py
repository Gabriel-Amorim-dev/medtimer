from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CadastroForm, PerfilForm


def pagina_cadastro(request):
    form = CadastroForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, f'Bem-vindo, {usuario.username}!')
            if request.user.is_authenticated:
                return redirect('dashboard')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    return render(request, 'users/cadastro.html', {'form': form})

def pagina_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            messages.success(request, f'Bem-vindo de volta!')
            next_url = request.POST.get('next', '').strip()
            return redirect(next_url if next_url else 'dashboard')
        else:
            messages.error(request, 'Usuário ou senha incorretos!')

    return render(request, 'users/login.html', {'next': request.GET.get('next', '')})

def pagina_logout(request):
    if request.method == 'POST':
        logout(request)
        messages.error(request, 'Logout realizado com sucesso!')
    return redirect('login')

@login_required
def pagina_perfil(request):
    form = PerfilForm(request.POST or None, instance=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso')
            return redirect('dashboard')
        else:
            messages.error(request, 'Perfil não pode ser atualizado. Corrija os erros')

    return render(request, 'users/perfil.html', {'form': form})
# Create your views here.
@login_required
def pagina_dashboard(request):
    return render(request, 'users/dashboard.html')