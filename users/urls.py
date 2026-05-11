from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.pagina_cadastro, name='cadastro'),
    path('login/',    views.pagina_login,    name='login'),
    path('logout/',   views.pagina_logout,   name='logout'),
    path('perfil/',   views.pagina_perfil,   name='perfil'),
    path('dashboard/', views.pagina_dashboard, name='dashboard'),
]