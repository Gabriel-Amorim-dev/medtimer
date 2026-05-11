from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name','last_name', 'email', 'horario_sono_inicio', 'horario_sono_fim'
    list_filter = 'email',
