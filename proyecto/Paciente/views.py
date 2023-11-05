from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Consulta(request):
    return render(request, 'Consultas-Paciente.html')

def Perfil(request):
    return render(request, 'Perfil-Paciente.html')
