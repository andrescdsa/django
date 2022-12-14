"""primerProyetoDjango URL Configuration

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

from deportes.views import deportes, listar_equipos_mundial
from webapp.views import bienvenido, adios, listar_alumnos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido, name="inicio"),
    path('goodbye/', adios),
    path('deportes/', deportes, name="deportes"),
    path('alumnos/listar_alumnos/', listar_alumnos, name="datos_alumnos"),
    path('deportes/futbol/equipos_mundial', listar_equipos_mundial, name="equipos_mundial"),
    path('deportes/futbol/masseleccion', listar_equipos_mundial, name="masseleccion"),
]
