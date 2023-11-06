from django.db import models

class Paciente(models.Model):
    idPaciente = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100)
    dpi = models.CharField(max_length=13)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    contraseña = models.CharField(max_length=128)
    role = models.CharField(max_length=1, default='3')

    class Meta:
        db_table = 'tbpacientes'
    
    def __str__(self):
        return f"{self.idPaciente}"

class Doctor(models.Model):
    idDoctor = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    colegiado = models.CharField(max_length=13, unique=True)
    telefono = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=128)
    role = models.CharField(max_length=1, default='2')

    class Meta:
        db_table = 'tbdoctor'
    
    def __str__(self):
        return f"{self.idDoctor}"

class Admin(models.Model):
    idAdmin = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=128)
    role = models.CharField(max_length=1, default='1')

    class Meta:
        db_table = 'tbadmin'
    
    def __str__(self):
        return f"{self.idAdmin}"

