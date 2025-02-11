from django.db import models

class Chata(models.Model):
    modelo = models.CharField(max_length=20) #charfield es un string
    marca = models.CharField(max_length=20)
    descripcion= models.TextField(null=True, blank=True) #textfield es un string mas largo
    # si quiero cambiar atributos y nombres y hago al migracion me va a crear una clase nueva, no va a
    # actualizarla. (Si le cambio solo el nombre no hay problema)
    
    