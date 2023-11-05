from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

"""
    path('Admin/', Admin.Consultas, name="adminInicio"),
    path('Admin/Perfil/', Admin.Perfil, name="adminPerfil"),
    path('Admin/Consultas/', Admin.Consultas_Resueltas, name="adminConsultas"),
    path('Admin/Registro-Pacientes/', Admin.Registro_Pacientes, name="adminPacientes"),
    path('Admin/Registro-Doctores/', Admin.Registro_Doctores, name="adminDoctores"),

"""


def Consultas(request):
    return render(request, 'Consultas-Admin.html')

def Consultas_Resueltas(request):
    return render(request, 'Consultas-Resueltas-Admin.html')

def Registro_Pacientes(request):
    return render(request, 'Registro-Paciente.html')

def Registro_Doctores(request):
    return render(request, 'Registro-Doctores.html')

def Perfil(request):
    return render(request, 'Perfil-Admin.html')