from django import forms
from Paciente.models import *

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['idPaciente', 'idDoctor', 'razon_visita','diagnostico', 'receta']