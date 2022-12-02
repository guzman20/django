from django.contrib import admin

from clientes.models import Cliente, Coche
from deporte.models import Jugador
from webapp.models import Persona

# Register your models here.
admin.site.register(Persona)
admin.site.register(Cliente)
admin.site.register(Coche)
admin.site.register(Jugador)
