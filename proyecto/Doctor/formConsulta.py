from django import forms
from Paciente.models import *

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['diagnostico', 'receta']