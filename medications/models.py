from django.db import models
from users.models import Usuario

class Medicamento(models.Model):
    usuario    = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='medicamentos')
    nome       = models.CharField(max_length=100)
    dosagem    = models.CharField(max_length=50)
    observacoes = models.TextField(blank=True)
    ativo      = models.BooleanField(default=True)
    criado_em  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} ({self.dosagem})'