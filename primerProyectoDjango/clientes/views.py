from django.shortcuts import render

from clientes.models import Cliente


# Create your views here.
def add_cliente(request):
    nombre = None
    apellidos = None
    dni = None
    email = None
    pagina_destino = "clientes/add.html"
    if request.method == "POST":
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        dni = request.POST['dni']
        email = request.POST['email']
        if nombre is not None and apellidos is not None and dni is not None and email is not None:
            pagina_destino = "bienvenido.html"
            cliente = Cliente(None, nombre, apellidos, dni, email)
            cliente.save()
    return render(request, pagina_destino)
