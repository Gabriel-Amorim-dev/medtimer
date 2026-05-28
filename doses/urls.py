from django.urls import path
from . import views

urlpatterns = [
    path('',                     views.dashboard, name='dash_doses'),
    path('<int:pk>/confirmar/',  views.confirmar, name='dose_confirmar'),
    path('<int:pk>/pular/',      views.pular,     name='dose_pular'),
]