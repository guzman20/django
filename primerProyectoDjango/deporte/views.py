from django.shortcuts import render


# Create your views here.
def deporte(request):
    informacion = {"titulo_tabla": "Deportes", "descripcion": "Los deporte son juegos de actividad fisica."}
    return render(request, "deporte.html", informacion)


def listar_equipos_mundial(request):
    titulo = None
    continente_filtro = None
    orden = None
    if request.method == 'POST':
        if 'continente' in request.POST.keys():
            continente_filtro = request.POST['continente']
        if 'orden' in request.POST['orden']:
            orden = request.POST['orden']
        titulo = request.POST['titulo']
    elif request.method == 'GET':
        titulo = request.GET['titulo']

    listar_equipos_mundial2 = [
        {"pais": "Qatar", "continente": "Asia", "mundiales_ganados": "0"},
        {"pais": "Inglaterra", "continente": "Europa", "mundiales_ganados": "1"},
        {"pais": "Brasil", "continente": "America", "mundiales_ganados": "5"},
        {"pais": "Portugal", "continente": "Europa", "mundiales_ganados": "0"},
        {"pais": "España", "continente": "Europa", "mundiales_ganados": "1"}
    ]

    if continente_filtro is not None:
        lista_selecciones = list(
            filter(lambda seleccion: seleccion["continente"] == continente_filtro, listar_equipos_mundial2))
    else:
        lista_selecciones = listar_equipos_mundial2
    if orden is not None:
        lista_selecciones = sorted(lista_selecciones, key=lambda seleccion: seleccion[orden])

    contexto = {"listado_selecciones": lista_selecciones, "titulo_tabla": titulo,
                "listado_continentes": ["Europa", "America", "Asia", "Africa", "Oceania"]}

    return render(request, "mundial/equipos.html", contexto)
