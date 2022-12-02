from django.db import models


# Create your models here.
class Jugador(models.Model):
    nombre = models.CharField(max_length=40, null=False)
    equipo = models.CharField(max_length=60)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=60)
    posicion = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} {self.nombre} {self.equipo} {self.edad} {self.nacionalidad} {self.posicion}"
