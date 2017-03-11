from __future__ import unicode_literals

from django.db import models

class Temporada(models.Model):
    Temporada = models.CharField(max_length=50)
    def __str__(self):
        return self.Temporada
class AreasControl(models.Model):
    AreasControl = models.CharField(max_length=50)
    def __str__(self):
        return self.AreasControl

class Estados(models.Model):
    Estados = models.CharField(max_length=50)
    def __str__(self):
        return self.Estados

class Meses(models.Model):
    Meses = models.CharField(max_length=50)
    Dias = models.IntegerField(default = 30)
    def __str__(self):
        return self.Meses

class Tarifa1x(models.Model):
    Nombre = models.CharField(max_length=200)
    Temp = models.ForeignKey(Temporada)
    Basico = models.FloatField(default = 0)
    Inter_Bajo = models.FloatField(default = 0)
    Inter_Medio = models.FloatField(default = 0)
    Excedente = models.FloatField(default = 0)
    CBasico = models.FloatField(default = 0)
    CInter_Bajo = models.FloatField(default = 0)
    CInter_Medio = models.FloatField(default = 0)
    CExcedente = models.FloatField(default = 0)
    DAC = models.IntegerField(default = 0)
    def __str__(self):
        return self.Nombre

class Ciudades(models.Model):
    Nombre = models.CharField(max_length=200)
    Estado = models.ForeignKey(Estados)
    AreaCont = models.ForeignKey(AreasControl)
    Tarifa = models.CharField(max_length=200, blank=True, null=True)
    Verano = models.ForeignKey(Meses, blank=True, null=True)
    def __str__(self):
        return self.Nombre

class DAC(models.Model):
    Fijo = models.FloatField(default = 0)
    AreaCont = models.ForeignKey(AreasControl)
    Temp = models.ForeignKey(Temporada, blank=True, null=True)
    Costo_kWh= models.FloatField(default = 0)
    Anio = models.FloatField(default = 0)
    Mes = models.ForeignKey(Meses, blank=True, null=True)
    def __str__(self):
        return str(self.id)

# class Tienda(models.Model):
#     Tienda = models.CharField(max_length=200)
#     demand = models.IntegerField(default = 0)
#     def __str__(self):
#         return self.Tienda

# class Demanda(models.Model):
#     cantidad = models.FloatField(null = True, blank = True)
#     costo = models.IntegerField(default = 0)
#     ruta = models.CharField(max_length=200)
#     fabric = models.ForeignKey(Fabrica)
#     tiend = models.ForeignKey(Tienda)
#     def __str__(self):
#         return self.ruta

# class Whiskas(models.Model):
#     animal = models.CharField(max_length=200)
#     prot = models.FloatField(default = 0)
#     cost = models.FloatField(default = 0)
#     fat = models.FloatField(default = 0)
#     fibre = models.FloatField(default = 0)
#     salt = models.FloatField(default = 0)
#     def __str__(self):
#         return self.animal
# # Create your models here.
