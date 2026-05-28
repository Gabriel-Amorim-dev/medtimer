from django.urls import path
from . import views

urlpatterns = [
    path('',               views.lista,  name='trat_lista'),
    path('novo/',          views.criar,  name='trat_criar'),
    path('<int:pk>/editar/', views.editar, name='trat_editar'),
    path('<int:pk>/pausar/', views.pausar, name='trat_pausar'),
]