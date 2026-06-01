from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Medicamento
from .forms import MedicamentoForm

@login_required
def listar(request):
    meds = Medicamento.objects.filter(usuario=request.user, ativo=True)
    return render(request, 'medications/lista.html', {'medicamentos': meds})

@login_required
def criar(request):
    form = MedicamentoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        med = form.save(commit=False)
        med.usuario = request.user
        med.save()
        messages.success(request, f'Medicação {med.nome} cadastrada com com sucesso!')
        return redirect('med_lista')
    return render(request, 'medications/form.html', {'form': form, 'titulo': 'Novo Medicamento'})
@login_required
def editar(request, pk):
    med = get_object_or_404(Medicamento, pk=pk, usuario=request.user)
    form = MedicamentoForm(request.POST or None, instance=med)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, 'Medicamento atualizado!')
        return redirect('med_lista')
    return render(request, 'medications/form.html', {'form': form, 'titulo': 'Editar Medicamento'})

@login_required
def deletar(request, pk):
    med = get_object_or_404(Medicamento, pk=pk, usuario=request.user)
    if request.method == 'POST':

        try:
            med.tratamento.delete()
        except Exception:
            pass

        med.ativo = False
        med.save()
        messages.success(request, f'Medicamento "{med.nome}" e seu tratamento foram removidos.')
        return redirect('med_lista')

    return render(request, 'medications/confirm_delete.html', {'objeto': med, 'nome': med.nome})