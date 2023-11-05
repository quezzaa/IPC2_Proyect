from django.shortcuts import redirect, render
from .formsRegistro import RegistroForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your views here.

from django.http import HttpResponse
# Create your views here.

def registrar_usuario(request):
    if request.method == 'GET':
        form = RegistroForm(request.POST)
        return render(request, 'Register-Paciente.html', {"form": form})
    else:
        
        if request.POST["contraseña"] == request.POST["confirmar_contraseña"]:
            try:
                usuario = User.objects.create_user(
                    usuario = form.cleaned_data['usuario'],
                    nombre = form.cleaned_data['nombre'],
                    dpi = form.cleaned_data['dpi'],
                    telefono = form.cleaned_data['telefono'],
                    direccion = form.cleaned_data['direccion'],
                    fecha_nacimiento = form.cleaned_data['fecha_nacimiento'],
                    contraseña = form.cleaned_data['contraseña']
                )
                usuario.save()
                login(request, usuario)
                return redirect('pacienteInicio')
            except IntegrityError:
                return render(request, 'Register-Paciente.html', {"form": form, "error": "Paciente ya existe."})
            
        return render(request, 'Register-Paciente.html', {"form": form, "error": "Las contraseñas no coinciden"})