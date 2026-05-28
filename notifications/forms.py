from django import forms
from .models import Notificacao

class NotificacaoFiltroForm(forms.Form):
    TIPO_CHOICES = [('', 'Todos os tipos')] + list(Notificacao.TIPOS)
    LIDA_CHOICES = [('', 'Todas'), ('0', 'Nao lidas'), ('1', 'Lidas')]

    tipo = forms.ChoiceField(
        choices=TIPO_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    lida = forms.ChoiceField(
        choices=LIDA_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )