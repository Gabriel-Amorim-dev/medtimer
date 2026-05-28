from django.db import models
from django.conf import settings
from doses.models import Dose

class Notificacao(models.Model):
    TIPOS = [('lembrete','Lembrete'),('escalada','Escalada'),('recalculo','Recalculo')]
    usuario    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notificacoes')
    dose       = models.ForeignKey(Dose, on_delete=models.CASCADE, related_name='notificacoes')
    tipo       = models.CharField(max_length=20, choices=TIPOS)
    enviada_em = models.DateTimeField(auto_now_add=True)
    lida       = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.tipo} — {self.usuario.username}'