from django.shortcuts import render
from django.http import HttpResponse
from .formConsulta import *
# Create your views here.


def Consultas(request):
    user = request.user
    idadmin = Admin.objects.get(usuario=user)
    idadmin = Admin.objects.get(idAdmin=idadmin.idAdmin)
    CPSin = Consulta.objects.filter(estado_consulta='1')
    CPRes = Consulta.objects.filter(estado_consulta='0')
    if request.method == 'GET':
        return render(request, 'Consultas-Admin.html', {"CPSin":CPSin, "CPRes":CPRes })
    else:
        return render(request, 'Consultas-Admin.html', {"CPSin":CPSin, "CPRes":CPRes })

def Registro_Pacientes(request):
    PacientesInfo = Paciente.objects.all()
    return render(request, 'Registro-Paciente.html',{"Pacientes": PacientesInfo})

def Registro_Doctores(request):
    DoctoresInfo = Doctor.objects.all()
    return render(request, 'Registro-Doctores.html',{"Doctores": DoctoresInfo})

def Perfil(request):
    user = request.user
    AdminInfo = Admin.objects.get(usuario=user)
    return render(request, 'Perfil-Admin.html', {"info": AdminInfo})