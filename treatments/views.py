from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pytz
from django.conf import settings
from django.utils.timezone import localdate, localtime
from datetime import datetime, timedelta
from .models import Tratamento
from doses.models import Dose
from .forms import TratamentoForm
from notifications.models import Notificacao
@login_required
def lista(request):
    from django.utils import timezone
    from doses.models import Dose

    hoje  = localdate()
    agora = timezone.now()

    tratamentos = Tratamento.objects.filter(
        medicamento__usuario=request.user
    ).select_related('medicamento')

    doses_hoje = Dose.objects.filter(
        tratamento__medicamento__usuario=request.user,
        horario_planejado__date=hoje,
        tratamento__status='ativo'
    ).select_related('tratamento__medicamento').order_by('horario_planejado')

    context = {
        'tratamentos': tratamentos,
        'hoje':        hoje,
        'atrasadas':   doses_hoje.filter(status='pendente', horario_planejado__lt=agora),
        'futuras':     doses_hoje.filter(status='pendente', horario_planejado__gte=agora,  horario_planejado__lte=agora + timedelta(minutes=30)),
        'tomadas':     doses_hoje.filter(status='tomado'),
        'perdidas':    doses_hoje.filter(status='perdido') }
    return render(request, 'treatments/lista.html', context)

@login_required
def criar(request):
    form = TratamentoForm(request.POST or None, usuario = request.user)
    if request.method == 'POST' and form.is_valid():
        t = form.save()
        _gerar_doses(t)
        messages.success(request, 'Tratamento criado e doses geradas!')
        return redirect('trat_lista')
    return render(request, 'treatments/form.html', {'form': form, 'titulo': 'Novo Tratamento'})

@login_required
def editar(request, pk):
    t = get_object_or_404(Tratamento, pk=pk, medicamento__usuario=request.user)
    form = TratamentoForm(request.POST or None, instance=t, usuario=request.user)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Tratamento atualizado')
        return redirect('trat_lista')
    return render(request, 'treatments/form.html', {'form': form, 'titulo': 'Editar Tratamento'})

@login_required
def pausar(request, pk):
    t = get_object_or_404(Tratamento, pk=pk, medicamento__usuario=request.user)
    if request.method == 'POST':
        t.status = 'pausado' if t.status == 'ativo' else 'ativo'
        t.save()
        messages.success(request, f'Tratamento {t.status}.')
    return redirect('trat_lista')

def _gerar_doses(tratamento):


    fuso          = pytz.timezone(settings.TIME_ZONE)
    intervalo     = timedelta(hours=tratamento.intervalo_horas)
    primeiro_naive = datetime.combine(tratamento.data_inicio, tratamento.horario_inicial)
    primeiro      = fuso.localize(primeiro_naive)
    horario_atual = primeiro
    doses         = []

    while True:
        if tratamento.data_fim and horario_atual.date() > tratamento.data_fim:
            break
        if not tratamento.data_fim and (horario_atual - primeiro).days > 90:
            break
        doses.append(Dose(
            tratamento=tratamento,
            horario_planejado=horario_atual,
            status='pendente'
        ))
        horario_atual += intervalo

    doses_criadas = Dose.objects.bulk_create(doses)
    
    if doses_criadas:
        primeira = doses_criadas[0]
        Notificacao.objects.create(
            usuario=tratamento.medicamento.usuario,
            dose=primeira,
            tipo='lembrete',
            lida=False
        )