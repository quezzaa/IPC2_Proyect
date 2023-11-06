from django import forms
from .models import *
from Login.models import *
from Login.formsRegistro import PacienteForm

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['razon_visita']