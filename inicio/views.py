from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Chata
from inicio.forms import CrearAuto


def inicio(request):
    # return HttpResponse("<h1>Esta es mi primera vista!</h1>")
    return render(request, 'inicio.html') #render sirve para cargar templates

def crear_auto(request):
    # print(request.GET) #puede servir para ver por donde se recibe la información. Normalmente viene por get por mas que no querramos.
    # print(request.POST)
    if request.method== "POST":
        formulario= CrearAuto(request.POST)
        if formulario.is_valid():
            formulario.cleaned_data #cleaned data es para validar informacion que es correcta o darla por correcta
            chata= Chata(
                modelo=formulario.cleaned_data.get('modelo'),
                marca=formulario.cleaned_data.get('marca'),
                descripcion=formulario.cleaned_data.get('descripcion')
                )
            chata.save()
    return render(request, 'inicio/crear_auto.html', {'formulario': formulario})

def listar_autos(request):
    autos = Chata.objects.all()
    return render(request, 'inicio/listar_autos.html', {'autos': autos})

