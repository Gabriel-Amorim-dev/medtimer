from django.db import models
from medications.models import Medicamento

class Tratamento(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('pausado', 'Pausado'),
        ('finalizado', 'Finalizado'),
    ]

    medicamento     = models.OneToOneField(Medicamento, on_delete=models.CASCADE, related_name='tratamento')
    intervalo_horas = models.PositiveIntegerField()
    horario_inicial = models.TimeField()
    data_inicio     = models.DateField()
    data_fim        = models.DateField(null=True, blank=True)
    status          = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo')

    def __str__(self):
        return f'Tratamento de {self.medicamento.nome} — {self.intervalo_horas}h/h'