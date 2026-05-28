from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render


from .models import Notificacao
from .forms import NotificacaoFiltroForm

@login_required
def lista(request):
    
    form  = NotificacaoFiltroForm(request.GET or None)
    notifs = Notificacao.objects.filter(
        usuario=request.user
    ).select_related('dose__tratamento__medicamento').order_by('-enviada_em')

    if form.is_valid():
        if form.cleaned_data.get('tipo'):
            notifs = notifs.filter(tipo=form.cleaned_data['tipo'])
        lida = form.cleaned_data.get('lida')
        if lida == '0':
            notifs = notifs.filter(lida=False)
        elif lida == '1':
            notifs = notifs.filter(lida=True)

    return render(request, 'notifications/lista.html', {'notificacoes': notifs, 'form': form})

@login_required
def marcar_lida(request, pk):
    notif = get_object_or_404(Notificacao, pk=pk, usuario=request.user)
    if request.method == 'POST':
        notif.lida = True
        notif.save()
    return redirect('notif_lista')

@login_required
def marcar_todas_lidas(request):
    if request.method == 'POST':
        Notificacao.objects.filter(usuario=request.user, lida=False).update(lida=True)
        messages.success(request, 'Todas as notificações marcadas como lidas.')
    return redirect('notif_lista')

@login_required
def limpar_todas(request):
    if request.method == 'POST':
        Notificacao.objects.filter(usuario=request.user).delete()
        messages.success(request, 'Todas as notificações foram removidas.')
    return redirect('notif_lista')