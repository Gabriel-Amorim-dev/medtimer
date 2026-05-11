from django.db import models
from users.models import Usuario
from doses.models import Dose

class Notificacao(models.Model):
    TIPO_CHOICES = [
        ('lembrete',  'Lembrete'),
        ('escalada',  'Escalada'),
        ('recalculo', 'Recálculo'),
    ]

    usuario    = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='notificacoes')
    dose       = models.ForeignKey(Dose, on_delete=models.CASCADE, related_name='notificacoes')
    tipo       = models.CharField(max_length=20, choices=TIPO_CHOICES)
    enviada_em = models.DateTimeField(auto_now_add=True)
    lida       = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.tipo} — {self.usuario.username} — {self.enviada_em.strftime("%d/%m %H:%M")}'