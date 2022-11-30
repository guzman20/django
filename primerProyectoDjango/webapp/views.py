from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def bienvenido(request):
    mensajes = {"mensaje1": "Valor1", "mensaje2": "Valor2"}
    return render(request, "bienvenido.html", mensajes)


def listado_alumnos(request):
    listado_alumnos2 = [
        {"nombre": "Nombre1", "apellido": "Apellido1", "dni": "11111A"},
        {"nombre": "Nombre2", "apellido": "Apellido2", "dni": "11111B"},
        {"nombre": "Nombre3", "apellido": "Apellido3", "dni": "11111C"}
    ]
    contexto = {"listado_alumnos": listado_alumnos2}
    return render(request, "gestion/alumnos.html", contexto)


def adios(request):
    return render(request, "adios.html")
