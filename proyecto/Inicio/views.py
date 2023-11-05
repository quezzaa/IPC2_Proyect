from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Inicio(request):
    return render(request,'index.html')

def Historia(request):
    return render(request,'historia.html')

def Formulario(request):
    return render(request,'formulario.html')

def Contacto(request):
    return render(request,'contactos.html')