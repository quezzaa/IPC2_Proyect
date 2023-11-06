from django.shortcuts import redirect, render
from django.http import HttpResponse
from .formConsulta import *
from Login.formsRegistro import AdminForm
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
    AdminInfo = Admin.objects.get(usuario=user.username)

    if request.method == 'POST':
        form = AdminForm(request.POST, instance=AdminInfo)
        if form.is_valid():
            user_instance = User.objects.get(username=user.username)
            user_instance.username = form.cleaned_data['usuario']
            user_instance.set_password(form.cleaned_data['contraseña'])
            user_instance.save()
            form.save()
            return redirect('Logout')
    else:
        form = AdminForm(instance=AdminInfo)

    return render(request, 'Perfil-Admin.html', {"info": AdminInfo, "form": form})

def eliminar_paciente(request, idPaciente):
    try:
        paciente = Paciente.objects.get(idPaciente=idPaciente)
        if request.method == 'POST':
            paciente.delete()
            return redirect('adminPacientes')
        else:
            return redirect(request.path)
    except Consulta.DoesNotExist:
        return redirect(request.path)
    
def eliminar_doctor(request, idDoctor):
    try:
        doc = Doctor.objects.get(idDoctor=idDoctor)
        if request.method == 'POST':
            doc.delete()
            return redirect('adminDoctores')
        else:
            return redirect(request.path)
    except Consulta.DoesNotExist:
        return redirect(request.path)
    
def eliminar_consulta(request, idConsulta):
    try:
        consulta = Consulta.objects.get(idConsulta=idConsulta)
        if request.method == 'POST':
            consulta.delete()
            return redirect('adminInicio')
        else:
            return redirect(request.path)
    except Consulta.DoesNotExist:
        return redirect(request.path)
    
def Ver_consulta(request, idConsulta):
    InfoConsulta = Consulta.objects.get(idConsulta=idConsulta)
    return render(request, 'ConsultaVer-Admin.html',{"InfoConsulta":InfoConsulta})