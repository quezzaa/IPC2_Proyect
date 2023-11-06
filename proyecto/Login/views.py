from django.shortcuts import redirect, render
from .formsRegistro import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your views here.

from django.http import HttpResponse
# Create your views here.

def registrar_paciente(request):
    if request.method == 'GET':
        form = PacienteForm(request.POST)
        return render(request, 'Register-Paciente.html', {"form": form})
    else:
        form = PacienteForm(request.POST)
        if request.POST["contraseña"] and request.POST["usuario"]:
            try:
                username = request.POST["usuario"]
                password = request.POST["contraseña"]

                # Crear un usuario con el formulario
                paciente = form.save(commit=False)
                paciente.role = '3' 

                user = User.objects.create_user(username=username, password=password)
                user = authenticate(username=username, password=password)
                if user is not None:
                    paciente.save()
                    login(request, user) 
                    return redirect('pacienteInicio')
            except IntegrityError:
                return render(request, 'Register-Paciente.html', {"form": form, "error": "Paciente ya existe."})
            
        return render(request, 'Register-Paciente.html', {"form": form, "error": "Contraseña o Usuario Invalidos"})
    
def registrar_doctor(request):
    if request.method == 'GET':
        form = DoctorForm(request.POST)
        return render(request, 'Register-Doctor.html', {"form": form})
    else:
        form = DoctorForm(request.POST)
        if request.POST["contraseña"] and request.POST["usuario"]:
            try:
                username = request.POST["usuario"]
                password = request.POST["contraseña"]

                # Crear un usuario con el formulario
                doctor = form.save(commit=False)
                doctor.role = '2' 

                user = User.objects.create_user(username=username, password=password)
                user = authenticate(username=username, password=password)
                if user is not None:
                    doctor.save()
                    login(request, user) 
                    return redirect('doctorInicio')
            except IntegrityError:
                return render(request, 'Register-Doctor.html', {"form": form, "error": "Doctor ya existe."})
            
        return render(request, 'Register-Doctor.html', {"form": form, "error": "Las contraseñas no coinciden"})
    
def LogIn(request):
    if request.method == 'GET':
        return render(request, 'LogIn.html', {"form": AuthenticationForm})
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'LogIn.html',{"form": AuthenticationForm, "error": "Contraseña o Usuario incorrecto"})
        else:
            userL = User.objects.get(username= request.POST['username'])
            try:
                paciente = Paciente.objects.get(usuario=userL)
                login(request, user) 
                return redirect('pacienteInicio')
            except Paciente.DoesNotExist:
                paciente = None
                try:
                    doctor = Doctor.objects.get(usuario=userL)
                    login(request, user) 
                    return redirect('doctorInicio')
                except Doctor.DoesNotExist:
                    doctor = None
                    try:
                        admin = Admin.objects.get(usuario=userL)
                        login(request, user) 
                        return redirect('adminInicio')
                    except Admin.DoesNotExist:
                        admin = None

def Logout(request):
    logout(request)
    redirect('Login')