from django.shortcuts import render, redirect

from deporte.models import Jugador

LISTA_SELECCIONES = [
    {"pais": "Qatar", "continente": "Asia", "mundiales_ganados": "0"},
    {"pais": "Inglaterra", "continente": "Europa", "mundiales_ganados": "1"},
    {"pais": "Brasil", "continente": "America", "mundiales_ganados": "5"},
    {"pais": "Portugal", "continente": "Europa", "mundiales_ganados": "0"},
    {"pais": "España", "continente": "Europa", "mundiales_ganados": "1"}
]
LISTA_CONTINENTES = ["Europa", "America", "Asia", "Africa", "Oceania"]
LISTA_EQUIPOS = ["Real Madrid", "Rayo Vallecano", "Atletico de madrid", "Barcelona FC"]
LISTA_NACIONALIDADES = ["Español", "Frances", "Belga", "Aleman", "Senegalés"]
LISTA_POSICIONES = ["Portero", "Defensa", "Centrocampista", "Delantero"]


# Create your views here.
def deporte(request):
    informacion = {"titulo_tabla": "Deportes", "descripcion": "Los deporte son juegos de actividad fisica."}
    return render(request, "deporte.html", informacion)


def listar_equipos_mundial(request):
    titulo = None
    continente_filtro = None
    orden = None
    lista_selecciones_ordenada = LISTA_SELECCIONES
    if request.method == 'POST':
        if 'continente' in request.POST.keys() and 'nombre' not in request.POST.keys():
            continente_filtro = request.POST['continente']
            if 'orden' in request.POST.keys():
                orden = request.POST['orden']
        titulo = request.POST['titulo']
    elif request.method == 'GET':
        titulo = request.GET['titulo']

    if continente_filtro in LISTA_CONTINENTES:
        lista_selecciones_ordenada = list(
            filter(lambda seleccion: seleccion["continente"] == continente_filtro, LISTA_SELECCIONES))

    if orden is not None:
        if orden == "mundiales_ganados":
            lista_selecciones_ordenada = sorted(LISTA_SELECCIONES, key=lambda seleccion: seleccion[orden], reverse=True)
        else:
            lista_selecciones_ordenada = sorted(LISTA_SELECCIONES, key=lambda seleccion: seleccion[orden], reverse=True)

    contexto = {"listado_selecciones": lista_selecciones_ordenada, "titulo_tabla": titulo,
                "listado_continentes": LISTA_CONTINENTES}

    return render(request, "mundial/equipos/lista_equipos.html", contexto)


def aniadir_equipo(request):
    nombre = None
    continente = None
    mundiales_ganados = None
    titulo = None
    if request.method == "POST":
        nombre = request.POST['nombre']
        continente = request.POST['continente']
        mundiales_ganados = request.POST['mundiales_ganados']
        if titulo not in request.GET.keys():
            titulo = "Selecciones mundial"
        else:
            titulo = request.GET['titulo']
    elif request.method == "GET":
        if titulo not in request.GET.keys():
            titulo = "Selecciones mundial"
        else:
            titulo = request.GET['titulo']
    if nombre is not None and continente is not None and mundiales_ganados is not None:
        LISTA_SELECCIONES.append(
            {"pais": str(nombre), "continente": str(continente), "mundiales_ganados": str(mundiales_ganados)})
        contexto = {"listado_selecciones": LISTA_SELECCIONES, "titulo_tabla": titulo,
                    "listado_continentes": LISTA_CONTINENTES}
        return render(request, "mundial/añadir_equipo.html", contexto)
    else:
        contexto = {"titulo_tabla": titulo, "listado_continentes": LISTA_CONTINENTES}
        return render(request, "mundial/equipos/añadir_equipo.html", contexto)


def listar_jugadores(request):
    lista_jugadores = Jugador.objects.all()
    contexto = {"lista_equipos": LISTA_EQUIPOS, "lista_nacionalidades": LISTA_NACIONALIDADES,
                "lista_posciones": LISTA_POSICIONES, "jugadores": lista_jugadores}
    if request.method == "POST":
        if "reset" in request.POST.keys():
            pass
        else:
            posicion = request.POST['posicion']
            nacionalidad = request.POST['nacionalidad']
            equipo = request.POST['equipo']
            if posicion != "":
                lista_jugadores = filter(lambda jugador: jugador.posicion == posicion, lista_jugadores)
            if nacionalidad != "":
                lista_jugadores = filter(lambda jugador: jugador.nacionalidad == nacionalidad, lista_jugadores)
            if equipo != "":
                lista_jugadores = filter(lambda jugador: jugador.equipo == equipo, lista_jugadores)
            contexto["jugadores"] = lista_jugadores
    elif request.method == "GET":
        pass
    return render(request, "mundial/jugadores/lista_jugadores.html", contexto)


def add_jugador(request):
    contexto = None
    nombre = None
    equipo = None
    nacionalidad = None
    edad = None
    posicion = None
    pagina_destino = "listado_jugadores_mundial"
    if request.method == "POST":
        nombre = request.POST['nombre']
        equipo = request.POST['equipo']
        nacionalidad = request.POST['nacionalidad']
        edad = request.POST['edad']
        posicion = request.POST['posicion']
        if "id_jugador" not in request.POST.keys():
            if nombre != "" and equipo != "" and edad != "" and nacionalidad != "" and posicion != "":
                jugador = Jugador(None, nombre, equipo, edad, nacionalidad, posicion)
                jugador.save()
            else:
                pagina_destino = "add_jugador"
        else:
            if nombre != "" and equipo != "" and edad != "" and nacionalidad != "" and posicion != "":
                id_jugador = request.POST['id_jugador']
                jugador = Jugador(id_jugador, nombre, equipo, edad, nacionalidad, posicion)
                jugador.save()
            else:
                pagina_destino = "add_jugador"
        lista_jugadores = Jugador.objects.all()
        contexto = {"lista_equipos": LISTA_EQUIPOS, "lista_nacionalidades": LISTA_NACIONALIDADES,
                    "lista_posciones": LISTA_POSICIONES, "jugadores": lista_jugadores}
        return redirect(pagina_destino)
    elif request.method == "GET":
        if "id_jugador" not in request.GET.keys():
            pagina_destino = "mundial/jugadores/add_jugador.html"
        else:
            id_jugador = request.GET['id_jugador']
            jugador = Jugador.objects.get(pk=id_jugador)
            contexto = {'jugador': jugador, 'id_jugador': id_jugador}
            pagina_destino = "mundial/jugadores/add_jugador.html"
    return render(request, pagina_destino, contexto)


def eliminar_jugador(request):
    id_jugador = request.GET['id_jugador']
    jugador = Jugador.objects.get(pk=id_jugador)
    jugador.delete()
    return redirect("listado_jugadores_mundial")


