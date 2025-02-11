from django import forms

class Chata():
    modelo = forms.CharField(max_length=20) 
    marca = forms.CharField(max_length=20)
    descripcion= forms.TextField(required=False, widget=forms.Textarea)