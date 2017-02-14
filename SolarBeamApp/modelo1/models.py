from __future__ import unicode_literals

from django.db import models

class Fabrica(models.Model):
    Fabrica = models.CharField(max_length=200)
    produccion = models.IntegerField(default = 0)
    def __str__(self):
        return self.Fabrica

class Tienda(models.Model):
    Tienda = models.CharField(max_length=200)
    demand = models.IntegerField(default = 0)
    def __str__(self):
        return self.Tienda

class Demanda(models.Model):
    cantidad = models.FloatField(null = True, blank = True)
    costo = models.IntegerField(default = 0)
    ruta = models.CharField(max_length=200)
    fabric = models.ForeignKey(Fabrica)
    tiend = models.ForeignKey(Tienda)
    def __str__(self):
        return self.ruta