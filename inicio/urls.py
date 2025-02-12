from django.urls import path
from inicio.views import inicio, crear_auto, listar_autos


urlpatterns= [
    path('', inicio, name="inicio"),
    path('crear-auto/', crear_auto, name="crear_auto"), #el primero es el nombre en la url, el segundo refiere a la vista y el nombre que es para citar la vista solo con el nombre
    path('listar-autos/', listar_autos, name="listar_autos"),
]
