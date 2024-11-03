from django.db import models

class Pacientes(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    # otros campos

    def __str__(self):
        return self.nombre
    
class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    # otros campos

    def __str__(self):
        return self.nombre


class Consultorio(models.Model):
    nombre = models.CharField(max_length=100)
    # otros campos

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    id_medico = models.ForeignKey('Medico', on_delete=models.CASCADE)
    id_consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE)
    id_paciente = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"Cita {self.id} - {self.fecha} {self.hora}"
    
