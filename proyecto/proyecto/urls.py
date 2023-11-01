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
from django.contrib import admin
from django.urls import path
from Inicio import views as Inicio
from Login import views as Login
from Paciente import views as Paciente
from Doctor import views as Doctor
from Admin import views as Admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Inicio.hello),
    path('login/', Login.helloLogin),
    path('Paciente/', Paciente.hello, name="pacienteInicio"),
    path('Paciente/Perfil/', Paciente.hello, name="pacientePerfil"),
    path('Doctor/', Doctor.hello, name="doctorInicio"),
    path('Doctor/Perfil/', Doctor.hello, name="doctorPerfil"),
    path('Doctor/Consultas-Respondidas/', Doctor.hello, name="doctorConsultas"),
    path('Admin/', Admin.hello, name="adminInicio"),
    path('Admin/Perfil/', Admin.hello, name="adminPerfil"),
    path('Admin/Consultas/', Admin.hello, name="adminConsultas"),
    path('Admin/Registro-Pacientes/', Admin.hello, name="adminPacientes"),
    path('Admin/Registro-Doctores/', Admin.hello, name="adminDoctores"),
]
