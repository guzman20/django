from django.db import models


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=40, null=False)
    apellidos = models.CharField(max_length=60)
    dni = models.CharField(max_length=9)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} {self.nombre} {self.apellidos} {self.dni} {self.email}"


class Coche(models.Model):
    matricula = models.CharField(max_length=40, null=False)
    marca = models.CharField(max_length=60, null=False)
    color = models.CharField(max_length=9)
    combustible = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.id} {self.matricula} {self.marca} {self.color} {self.combustible} {self.cliente}"
