from django import forms
from .models import Medicamento

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nome', 'dosagem', 'observacoes']
        widgets = {
            'nome':        forms.TextInput(attrs={'class':'form-control','placeholder':'Ex: Paracetamol'}),
            'dosagem':     forms.TextInput(attrs={'class':'form-control','placeholder':'Ex: 500mg'}),
            'observacoes': forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Ex: tomar em jejum'})
        }
