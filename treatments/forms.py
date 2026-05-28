from django import forms
from .models import Tratamento

class TratamentoForm(forms.ModelForm):
    class Meta:
        model = Tratamento
        fields =['medicamento', 'intervalo_horas', 'horario_inicial', 'data_inicio','data_fim']
        widgets = {
            'medicamento':     forms.Select(attrs={'class':'form-control'}),
            'intervalo_horas': forms.NumberInput(attrs={'class':'form-control','placeholder':'Ex: 8'}),
            'horario_inicial': forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'data_inicio':     forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'data_fim':        forms.DateInput(attrs={'class':'form-control','type':'date'}),
        }

    def __init__(self, *args, usuario=None, **kwargs):
        super().__init__(*args, **kwargs)
        if usuario:
            self.fields['medicamento'].queryset = \
                self.fields['medicamento'].queryset.filter(usuario=usuario, ativo=True)