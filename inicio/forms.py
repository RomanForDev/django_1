from django import forms

class CrearAuto(forms.Form):
    modelo = forms.CharField(max_length=20) 
    marca = forms.CharField(max_length=20)
    descripcion= forms.CharField(required=False, widget=forms.Textarea) #required es por si es un campo que sea requerido si o si o no y widget es para poenr un input pero que se vea diferente (como una casilla)
    