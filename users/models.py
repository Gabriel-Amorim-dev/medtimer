from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # email já existe no AbstractUser, só adiciona a constraint
    horario_sono_inicio = models.TimeField(null=True, blank=True)
    horario_sono_fim = models.TimeField(null=True, blank=True)


    def __str__(self):
        return self.username