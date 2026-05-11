from django.contrib import admin

from doses import models

@admin.register(models.Dose)
class DosesAdmin(admin.ModelAdmin):
    list_display = 'id', 'tratamento', 'horario_planejado', 'horario_real', 'status', 'recalculada'
    list_filter = ('status', 'recalculada')

# Register your models here.
