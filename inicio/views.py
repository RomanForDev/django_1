from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Chata
from inicio.forms import crear


def inicio(request):
    # return HttpResponse("<h1>Esta es mi primera vista!</h1>")
    return render(request, 'inicio.html') #render sirve para cargar templates

def crear_auto(request):
    formulario= crear_auto
    return render(request, 'inicio/crear_auto.html', {'formulario': formulario})

