from django import forms

class EmpleadoFormulario(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    cargo = forms.CharField()



class ClienteFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    

class BebidasFormulario(forms.Form):
    
    nombre = forms.CharField()
    licuado = forms.CharField()
    cafe = forms.CharField()
    cocacola = forms.CharField()