from django import forms
from .models import *

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['usuario', 'nombre', 'dpi', 'telefono', 'direccion', 'fecha_nacimiento', 'contraseña']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['usuario', 'nombre', 'colegiado', 'especialidad', 'telefono' ,'contraseña']

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['usuario','nombre','contraseña']
    


