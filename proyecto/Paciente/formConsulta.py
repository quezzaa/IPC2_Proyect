from django import forms
from .models import *

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['razon_visita']