from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def bienvenido(request):
    ##return HttpResponse("Hola")
    ##return render(request, "bienvenido.html")
    mensajes = {"mensaje1": "Hola desde el mensaje 1", "mensaje2": "Hola desde el mensaje 2"}
    return render(request, "bienvenido.html", mensajes)


def adios(request):
    return render(request, "adios.html")

def listar_alumnos(request):
    listado_alumno = [
        {"nombre":"nombre1", "apellido": "apellido1", "dni": "dni1"},
        {"nombre": "nombre2", "apellido": "apellido2", "dni": "dni2"},
        {"nombre": "nombre3", "apellido": "apellido3", "dni": "dni3"}
    ]
    contexto = {"listado_alumnos": listado_alumno}
    return render(request, "gestion/alumnos.html", contexto)
