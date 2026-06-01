from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from doses.models import Dose
from notifications.models import Notificacao

class Command(BaseCommand):
    help = 'Gera notificações para doses nos próximos 30 minutos'

    def handle(self, *args, **kwargs):
        agora = timezone.now()
        janela = agora + timedelta(minutes=30)

        doses_proximas = Dose.objects.filter(
            status='pendente',
            horario_planejado__gte=agora,
            horario_planejado__lte=janela,
            tratamento__status='ativo'
        ).select_related('tratamento__medicamento__usuario')

        ja_notificadas = set(
            Notificacao.objects.filter(
                dose__in=doses_proximas,
                tipo='lembrete'
            ).values_list('dose_id', flat=True)
        )

        novas = [
            Notificacao(
                usuario=dose.tratamento.medicamento.usuario,
                dose=dose,
                tipo='lembrete',
                lida=False
            )
            for dose in doses_proximas
            if dose.id not in ja_notificadas
        ]

        Notificacao.objects.bulk_create(novas)
        self.stdout.write(f'{len(novas)} notificação(ões) criada(s).')