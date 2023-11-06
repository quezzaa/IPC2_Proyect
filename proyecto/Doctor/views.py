from django.shortcuts import render
from django.http import HttpResponse
from .formConsulta import *
# Create your views here.

def Inicio(request):
    return render(request, 'Inicio-Doctor.html')

def Consultas(request):
    user = request.user
    iddoctor = Doctor.objects.get(usuario=user)
    iddoctor = Doctor.objects.get(idDoctor=iddoctor.idDoctor)
    CPSin = Consulta.objects.filter(estado_consulta='1')
    CPRes = Consulta.objects.filter(idDoctor=iddoctor, estado_consulta='0')

    if request.method == 'GET':
        return render(request, 'Consultas-Doctor.html', {"CPSin":CPSin, "CPRes":CPRes })
    else:
        print()



    return render(request, 'Consultas-Doctor.html')

def ConsultasResueltas(request):
    return render(request, 'Resueltas-Doctor.html')

def Perfil(request):
    user = request.user
    DoctorInfo = Doctor.objects.get(usuario=user)
    return render(request, 'Perfil-Doctor.html', {"info": DoctorInfo})
