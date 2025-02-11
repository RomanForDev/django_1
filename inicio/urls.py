from django.urls import path
from inicio.views import inicio, crear_auto


urlpatterns= [
    path('', inicio, name="inicio"),
    path('crear_auto/', crear_auto, name="crear_auto")
]
