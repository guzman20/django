"""primerProyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from clientes.views import add_cliente
from deporte.views import deporte, listar_equipos_mundial, aniadir_equipo, listar_jugadores, add_jugador, \
    eliminar_jugador
from webapp.views import bienvenido, adios, listado_alumnos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', bienvenido, name="inicio"),
    path('goodbye/', adios),
    path('deporte/', deporte, name="deporte"),
    path('listado_alumnos/', listado_alumnos, name="listado_alumnos"),
    path('deporte/mundial/equipos/lista_equipos', listar_equipos_mundial, name="listado_equipos_mundial"),
    path('deporte/mundial/equipos/añadir_equipo/', aniadir_equipo, name="aniadir_equipo"),
    path('clientes/add', add_cliente, name="add_cliente"),
    path('deporte/mundial/jugadores/lista_jugadores', listar_jugadores, name="listado_jugadores_mundial"),
    path('deporte/mundial/jugadores/add_jugador', add_jugador, name="add_jugador"),
    path('deporte/mundial/jugadores/eliminar_jugador', eliminar_jugador, name="eliminar_jugador")
]
