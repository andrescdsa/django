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
        {"seleccion":"Brasil", "continente": "Sudámerica", "ganados": 5},
        {"seleccion":"Alemania", "continente": "Europa", "ganados": 4},
        {"seleccion":"Italia", "continente": "Europa", "ganados": 4},
        {"seleccion":"Argentina", "continente": "Sudámerica", "ganados": 2},
        {"seleccion":"Francia", "continente": "Europa", "ganados": 2},
        {"seleccion": "Uruguay", "continente": "Sudámerica", "ganados": 2},
        {"seleccion": "Inglaterra", "continente": "Europa", "ganados": 1},
        {"seleccion": "España", "continente": "Europa", "ganados": 1}
    ]

    datos = {"listado_selecciones" : listado_selecciones}
    return render(request, "selecciones.html", datos)