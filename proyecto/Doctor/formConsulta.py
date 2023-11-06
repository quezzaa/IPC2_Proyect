from django import forms
from Paciente.models import *

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['diagnostico', 'receta']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['usuario', 'nombre', 'colegiado', 'especialidad', 'telefono' ,'contraseña']

class ConsultaDoctorForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['diagnostico', 'receta']