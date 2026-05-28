from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import Dose

@login_required
def dashboard(request):  

    hoje = timezone.now().date()
    agora = timezone.now()

    call_command('gerar_notificacoes')
    
    doses_hoje = Dose.objects.filter(
        tratamento__medicamento__usuario=request.user,
        horario_planejado__date=hoje,
        tratamento__status='ativo'
    ).select_related('tratamento__medicamento').order_by('horario_planejado')

    context = {
        'atrasadas': doses_hoje.filter(status='pendente', horario_planejado__lt=agora),
        'futuras': doses_hoje.filter(status='pendente', horario_planejado__gte=agora,  horario_planejado__lte=agora + timedelta(minutes=30)),
        'tomadas': doses_hoje.filter(status='tomado'),
        'perdidas': doses_hoje.filter(status='perdido'),
        'hoje': hoje,
    }
    return render(request, 'doses/dashboard.html', context)

@login_required
def confirmar(request, pk):
    dose = get_object_or_404(Dose, pk=pk, tratamento__medicamento__usuario=request.user)
    if request.method == 'POST':
        if dose.status != 'pendente':
            messages.warning(request, 'Dose ja registrada.')
            return redirect('dashboard')
        tr = timezone.now()
        dose.horario_real = tr
        dose.status       = 'tomado'
        margem            = timedelta(minutes=30)
        if tr > dose.horario_planejado + margem:
            dose.recalculada = True
            dose.save()
            _recalcular(dose.tratamento, tr)
            messages.success(request, f'Dose confirmada com atraso, Proximas doses recalculadas a partir das {tr.strftime("%H:%M")}.')
        else:
            dose.save()
            messages.success(request, 'Dose confirmada no horario')
    return redirect('dashboard')

@login_required
def pular(request, pk):
    dose = get_object_or_404(Dose, pk=pk, tratamento__medicamento__usuario=request.user)
    if request.method == 'POST':
        dose.status = 'perdido'
        dose.save()
        messages.warning(request, 'Dose marcada como perdida.')
    return redirect('dashboard')

def _recalcular(tratamento, horario_real):
    intervalo     = timedelta(hours=tratamento.intervalo_horas)
    doses_futuras = Dose.objects.filter(
        tratamento=tratamento,
        status='pendente',
        horario_planejado__gt=horario_real
    ).order_by('horario_planejado')
    novo = horario_real + intervalo
    for d in doses_futuras:
        d.horario_planejado = novo
        d.recalculada       = True
        novo               += intervalo
    Dose.objects.bulk_update(doses_futuras, ['horario_planejado','recalculada'])