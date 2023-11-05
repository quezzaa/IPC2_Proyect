from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Inicio(request):
    return render(request, 'Inicio-Doctor.html')

def Consultas(request):
    return render(request, 'Consultas-Doctor.html')

def ConsultasResueltas(request):
    return render(request, 'Resueltas-Doctor.html')

def Perfil(request):
    return render(request, 'Perfil-Doctor.html')
