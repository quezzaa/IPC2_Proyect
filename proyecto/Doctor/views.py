from django.shortcuts import redirect, render
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
    DoctorInfo = Doctor.objects.get(usuario=user.username)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=DoctorInfo)
        if form.is_valid():
            user_instance = User.objects.get(username=user.username)
            user_instance.username = form.cleaned_data['usuario']
            user_instance.set_password(form.cleaned_data['contraseña'])
            user_instance.save()
            form.save()
            return redirect('Logout')
    else:
        form = DoctorForm(instance=DoctorInfo)

    return render(request, 'Perfil-Doctor.html', {"info": DoctorInfo, "form": form})

def ConsultaIndividual(request, idConsulta):
    user = request.user
    iddoctor = Doctor.objects.get(usuario=user)
    iddoctor = Doctor.objects.get(idDoctor=iddoctor.idDoctor)
    InfoConsulta = Consulta.objects.get(idConsulta=idConsulta)
    if request.method == 'POST':
        form = ConsultaDoctorForm(request.POST, instance=InfoConsulta)
        if form.is_valid():
            consultaRes = form.save(commit=False)
            consultaRes.estado_consulta = '0'
            consultaRes.idDoctor = iddoctor
            consultaRes.save()
            return redirect('doctorInicio')
    else:
        form = ConsultaDoctorForm(instance=InfoConsulta)      
    
    return render(request, 'Consultas-Individual-Doctor.html',{"form": form, "InfoConsulta":InfoConsulta})

