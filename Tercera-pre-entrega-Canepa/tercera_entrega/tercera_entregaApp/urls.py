from django.contrib import admin
from django.urls import path
from tercera_entregaApp.views import *

urlpatterns = [
   
   path('', inicio, name="inicio"),
   
   path('empleadoformulario/', empleadoFormulario, name="empleadoformulario"),
   
   path('clienteformulario/', clienteFormulario, name="clienteformulario"),

   path('busquedacliente/', busquedaCliente, name="busquedacliente"),

   path('bebidasformulario/', BebidasFormulario, name="bebidasformulario"),
   
   path('buscar/', buscar, name="Buscar"),

]