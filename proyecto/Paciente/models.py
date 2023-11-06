from django.db import models
from django.utils import timezone
from Login.models import Paciente, Doctor, Admin

class Consulta(models.Model):
    idConsulta = models.AutoField(primary_key=True)
    idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    idDoctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha_consulta = models.DateTimeField(default=timezone.now)
    razon_visita = models.TextField()
    diagnostico = models.TextField()
    receta = models.TextField()
    estado_consulta = models.CharField(max_length=1, default='1')

    class Meta:
        db_table = 'tbconsultas'

    def __str__(self):
        return self.idConsulta, self.idPaciente, self.idDoctor, self.fecha_consulta, self.razon_visita, self.diagnostico, self.receta, self.estado_consulta