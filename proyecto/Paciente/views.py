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
    PacienteInfo = Paciente.objects.get(usuario=user.username)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=PacienteInfo)
        if form.is_valid():
            user_instance = User.objects.get(username=user.username)
            user_instance.username = form.cleaned_data['usuario']
            user_instance.set_password(form.cleaned_data['contraseña'])
            user_instance.save()
            form.save()
            return redirect('Logout')
    else:
        form = PacienteForm(instance=PacienteInfo)

    return render(request, 'Perfil-Paciente.html', {"info": PacienteInfo, "form": form})

def ConsultaIndividual(request, idConsulta):
    InfoConsulta = Consulta.objects.get(idConsulta=idConsulta)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=InfoConsulta)
        if form.is_valid():
            consultaRes = form.save(commit=False)
            consultaRes.save()
            return redirect('pacienteInicio')
    else:
        form = ConsultaForm(instance=InfoConsulta)      
    
    return render(request, 'Consultas-Individual-Paciente.html',{"form": form, "InfoConsulta":InfoConsulta})

def ConsultaIndividualRes(request, idConsulta):
    InfoConsulta = Consulta.objects.get(idConsulta=idConsulta)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=InfoConsulta)
        if form.is_valid():
            consultaRes = form.save(commit=False)
            consultaRes.save()
            return redirect('pacienteInicio')
    else:
        form = ConsultaForm(instance=InfoConsulta)      
    
    return render(request, 'Consultas-Individual-Paciente-Res.html',{"form": form, "InfoConsulta":InfoConsulta})

def eliminar_consulta(request, idConsulta):
    try:
        consulta = Consulta.objects.get(idConsulta=idConsulta)
        if request.method == 'POST':
            consulta.delete()
            return redirect('pacienteInicio')
        else:
            return redirect(request.path)
    except Consulta.DoesNotExist:
        return redirect(request.path)