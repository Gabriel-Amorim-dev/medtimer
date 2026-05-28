from django.urls import path
from . import views

urlpatterns = [
    path('',                    views.lista,             name='notif_lista'),
    path('<int:pk>/lida/',      views.marcar_lida,       name='notif_lida'),
    path('marcar-todas/',       views.marcar_todas_lidas,name='notif_todas_lidas'),
    path('notificacoes/limpar/',       views.limpar_todas, name='notif_limpar_todas'),
]