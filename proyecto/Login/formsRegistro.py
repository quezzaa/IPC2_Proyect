from django import forms

class RegistroForm(forms.Form):
    usuario = forms.CharField(max_length=100)
    nombre = forms.CharField(max_length=100)
    dpi = forms.CharField(max_length=13)
    telefono = forms.CharField(max_length=15)
    direccion = forms.CharField(max_length=200)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput)
    contraseña = forms.CharField(widget=forms.PasswordInput)
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput)
