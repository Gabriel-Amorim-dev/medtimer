from django.urls import path
from . import views

urlpatterns = [
    path('',              views.listar,   name='med_lista'),
    path('novo/',         views.criar,   name='med_criar'),
    path('<int:pk>/editar/',  views.editar,  name='med_editar'),
    path('<int:pk>/deletar/', views.deletar, name='med_deletar'),
]