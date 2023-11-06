from django.shortcuts import redirect, render
from django.http import HttpResponse
from .formConsulta import *
#from .models import *
# Create your views here.

def Consultas(request):
    user = request.user
    idpaciente = Paciente.objects.get(usuario=user)
    idpaciente = Paciente.objects.get(idPaciente=idpaciente.idPaciente)
    if request.method == 'GET':
        CPSin = Consulta.objects.filter(idPaciente=idpaciente, estado_consulta='1')
        CPRes = Consulta.objects.filter(idPaciente=idpaciente, estado_consulta='0')
        return render(request, 'Consultas-Paciente.html', {"form": ConsultaForm(request.POST), "CPSin":CPSin, "CPRes":CPRes })
    else:
        form = ConsultaForm(request.POST)
        if request.POST["razon_visita"]:
            consulta = form.save(commit=False)
            consulta.idPaciente = idpaciente
            consulta.save()
            return redirect(request.path)
        else:
            return render(request, 'Consultas-Paciente.html', {"form": ConsultaForm(request.POST), "error":"Sin enviar, Llenar los datos correspondientes!", "CPSin":CPSin, "CPRes":CPRes })

def Perfil(request):
    user = request.user
    PacienteInfo = Paciente.objects.get(usuario=user)
    return render(request, 'Perfil-Paciente.html', {"info": PacienteInfo})
