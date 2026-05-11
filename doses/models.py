from django.db import models
from treatments.models import Tratamento

class Dose(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('tomado',   'Tomado'),
        ('perdido',  'Perdido'),
    ]

    tratamento        = models.ForeignKey(Tratamento, on_delete=models.CASCADE, related_name='doses')
    horario_planejado = models.DateTimeField()
    horario_real      = models.DateTimeField(null=True, blank=True)
    status            = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    recalculada       = models.BooleanField(default=False)

    class Meta:
        ordering = ['horario_planejado']

    def __str__(self):
        return f'{self.tratamento.medicamento.nome} — {self.horario_planejado.strftime("%d/%m %H:%M")} [{self.status}]'