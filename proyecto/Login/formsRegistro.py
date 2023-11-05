from django import forms

class RegistroPaciente(forms.Form):
    usuario = forms.CharField(max_length=100)
    nombre = forms.CharField(max_length=100)
    dpi = forms.CharField(max_length=13)
    telefono = forms.CharField(max_length=15)
    direccion = forms.CharField(max_length=200)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput)
    contraseña = forms.CharField(widget=forms.PasswordInput)
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput)

class RegistroDoctor(forms.Form):
    usuario = forms.CharField(max_length=100)
    nombre = forms.CharField(max_length=100)
    colegiado = forms.CharField(max_length=50)
    especialidad = forms.CharField(max_length=15)
    telefono = forms.CharField(max_length=200)
    contraseña = forms.CharField(widget=forms.PasswordInput)
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput)
    

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=100)
    contraseña = forms.CharField(widget=forms.PasswordInput)


