from django.contrib import admin
from .models import Tratamento

@admin.register(Tratamento)
class TratamentoAdmin(admin.ModelAdmin):
    list_display = ('medicamento', 'intervalo_horas', 'status', 'data_inicio')
    list_filter  = ('status',)