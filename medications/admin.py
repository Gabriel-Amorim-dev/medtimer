from django.contrib import admin
from .models import Medicamento

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display  = ('nome', 'dosagem', 'usuario', 'ativo', 'criado_em')
    list_filter   = ('ativo',)
    search_fields = ('nome',)