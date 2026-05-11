from django.contrib import admin

from medications import models

@admin.register(models.Medicamento)
class DosesAdmin(admin.ModelAdmin):
    list_display = 'id', 'usuario', 'nome', 'dosagem', 'observacoes', 'ativo', 'criado_em'


# Register your models here.
