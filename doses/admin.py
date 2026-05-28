from django.contrib import admin
from .models import Dose

@admin.register(Dose)
class DoseAdmin(admin.ModelAdmin):
    list_display  = ('tratamento', 'horario_planejado', 'horario_real', 'status', 'recalculada')
    list_filter   = ('status', 'recalculada')