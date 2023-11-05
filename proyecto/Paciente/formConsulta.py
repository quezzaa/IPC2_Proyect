from django import forms

class ConsultaPacienteForm (forms.Form):
    idPaciente = forms.CharField(max_length=4)
    idDoctor = forms.CharField(max_length=4)
    fecha_consulta = forms.DateField(widget=forms.DateInput)
    razon_visita = forms.CharField(max_length=200)
    diagnostico = forms.CharField(max_length=200)
    receta = forms.CharField(max_length=200)
    estado_consulta = forms.CharField(max_length=1)