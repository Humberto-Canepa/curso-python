from django.db import models

#defino un empleado
class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre}'


#Defino un cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f'{self.nombre}'
    

#Defino las bebidas
class Bebidas(models.Model):
    nombre =   models.CharField(max_length=50)
    licuado =  models.CharField(max_length=50)
    cafe =     models.CharField(max_length=50)
    cocacola = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre}'