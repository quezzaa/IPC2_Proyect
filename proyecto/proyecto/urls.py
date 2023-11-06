"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Inicio import views as Inicio
from Login import views as Login
from Paciente import views as Paciente
from Doctor import views as Doctor
from Admin import views as Admin

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', Inicio.Inicio, name = "Inicio"),
    path('Historia/', Inicio.Historia, name = "Historia"),
    path('Formulario/', Inicio.Formulario, name = "Formulario"),
    path('Contacto/', Inicio.Contacto, name = "Contacto"),

    path('login/', Login.LogIn, name="Login"),
    path('login/pacientes/', Login.registrar_paciente, name="RegisterPacientes"),
    path('login/doctores/', Login.registrar_doctor, name="RegisterDoctores"),
    path('login/admin/', Login.registrar_admin, name="RegisterAdministradores"),

    path('Paciente/', Paciente.Consultas, name="pacienteInicio"),
    path('Paciente/Perfil/', Paciente.Perfil, name="pacientePerfil"),

    path('Paciente/<int:idConsulta>/', Paciente.ConsultaIndividual, name="pacienteConsultaIndividual"),
    path('Paciente/Respondidas/<int:idConsulta>/', Paciente.ConsultaIndividualRes, name="pacienteConsultaIndividualRes"),
    path('Paciente/eliminar/<int:idConsulta>/', Paciente.eliminar_consulta, name="eliminarConsultaPaciente"),

    path('Doctor/', Doctor.Consultas, name="doctorInicio"), 
    path('Doctor/Perfil/', Doctor.Perfil, name="doctorPerfil"),

    path('Doctor/<int:idConsulta>/', Doctor.ConsultaIndividual, name="doctorConsultaIndividual"),

    path('Admin/Perfil/', Admin.Perfil, name="adminPerfil"),
    path('Admin/Registro-Pacientes/', Admin.Registro_Pacientes, name="adminPacientes"),
    path('Admin/Registro-Doctores/', Admin.Registro_Doctores, name="adminDoctores"),
    path('Admin/', Admin.Consultas, name="adminInicio"),

    path('Admin/eliminar/<int:idConsulta>/', Admin.eliminar_consulta, name="eliminarConsultaAdmin"),
    path('Admin/Consulta/<int:idConsulta>/', Admin.Ver_consulta, name="adminConsultaIndividual"),

    path('Admin/Registro-Pacientes/<int:idPaciente>/', Admin.eliminar_paciente, name="adminPacientesIndividual"),
    path('Admin/Registro-Doctores/<int:idDoctor>/', Admin.eliminar_doctor, name="adminDoctoresIndividual"),

    path('login/', Login.Logout, name="Logout"),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)