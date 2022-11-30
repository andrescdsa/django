from django.shortcuts import render


# Create your views here.
# Create your views here.
def deportes(request):
    ##return HttpResponse("Hola")
    ##return render(request, "bienvenido.html")
    mensajes = {"titulopag": "Descripción Deporte", "descripcion": "Deporte con una pelota y 22 jugadores"}
    return render(request, "deportes.html", mensajes)


def listar_equipos_mundial(request):
    listado_selecciones = [
        {"seleccion": "Brasil", "continente": "Sudámerica", "ganados": 5},
        {"seleccion": "Alemania", "continente": "Europa", "ganados": 4},
        {"seleccion": "Italia", "continente": "Europa", "ganados": 4},
        {"seleccion": "Argentina", "continente": "Sudámerica", "ganados": 2},
        {"seleccion": "Francia", "continente": "Europa", "ganados": 2},
        {"seleccion": "Uruguay", "continente": "Sudámerica", "ganados": 2},
        {"seleccion": "Inglaterra", "continente": "Europa", "ganados": 1},
        {"seleccion": "España", "continente": "Europa", "ganados": 1}
    ]
    continente = None
    continentemas = None
    seleccion = None
    ganados = None
    action = None

    if request.method == 'POST':
        action = request.POST['action']
        continente = request.POST['continente']
        titulo_tabla = request.POST['titulo']
        continentemas = request.POST['continentemas']
        seleccion = request.POST['seleccion']
        ganados = request.POST['ganados']
        if action == 'equipos_mundial':
            if not continente == None:
                listado_selecciones = list(
                    filter(lambda seleccion: seleccion["continente"] == continente, listado_selecciones))
        elif action == 'masseleccion':
            if not seleccion == None and ganados == None and continentemas == None:
                masseleccion = {"seleccion": seleccion, "continente": continentemas, "ganados": ganados}
                listado_selecciones = listado_selecciones.append(masseleccion)
    elif request.method == 'GET':
        titulo_tabla = request.GET['titulo']

    datos = {"listado_selecciones": listado_selecciones, " titulo_tabla": titulo_tabla,
             "listado_continentes": ["Europa", "America", "Asia", "Africa", "Oceania"]}
    return render(request, "selecciones.html", datos)
