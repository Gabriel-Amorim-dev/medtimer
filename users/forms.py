from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class CadastroForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='E-mail',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'seu@email.com'
        })
    )

    class Meta:
        model  = Usuario
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'username': 'Nome de usuario'}
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: joao_silva'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirme a senha'


class PerfilForm(forms.ModelForm):
    class Meta:
        model  = Usuario
        fields = [
            'first_name',
            'last_name',
            'email',
            'horario_sono_inicio',
            'horario_sono_fim',
        ]
        labels = {
            'first_name':          'Nome',
            'last_name':           'Sobrenome',
            'email':               'E-mail',
            'horario_sono_inicio': 'Inicio do periodo de sono',
            'horario_sono_fim':    'Fim do periodo de sono',
        }
        widgets = {
            'first_name':          forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':           forms.TextInput(attrs={'class': 'form-control'}),
            'email':               forms.EmailInput(attrs={'class': 'form-control'}),
            'horario_sono_inicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'horario_sono_fim':    forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }