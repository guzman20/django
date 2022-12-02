from django.db import models


# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=60)
    dni = models.CharField(max_length=9)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} {self.nombre} {self.apellidos} {self.dni} {self.email}"
