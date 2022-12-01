from django.shortcuts import render

LISTA_SELECCIONES = [
    {"pais": "Qatar", "continente": "Asia", "mundiales_ganados": "0"},
    {"pais": "Inglaterra", "continente": "Europa", "mundiales_ganados": "1"},
    {"pais": "Brasil", "continente": "America", "mundiales_ganados": "5"},
    {"pais": "Portugal", "continente": "Europa", "mundiales_ganados": "0"},
    {"pais": "España", "continente": "Europa", "mundiales_ganados": "1"}
]
LISTA_CONTINENTES = ["Europa", "America", "Asia", "Africa", "Oceania"]


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

    return render(request, "mundial/equipos.html", contexto)


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
        return render(request, "mundial/añadir_equipo.html", contexto)
