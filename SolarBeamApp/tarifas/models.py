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

class Anio(models.Model):
    Anio = models.IntegerField(default = 2000)
    def __str__(self):
        return str(self.Anio)

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
    Anio = models.ForeignKey(Anio, blank=True, null=True)
    def __str__(self):
        return self.Nombre

class Tarifa2(models.Model):
    Mes = models.ForeignKey(Meses, blank=True, null=True)
    Anio = models.ForeignKey(Anio, blank=True, null=True)
    Basico = models.FloatField(default = 0)
    Inter = models.FloatField(default = 0)
    Excedente = models.FloatField(default = 0)
    CBasico = models.FloatField(default = 50)
    CInter = models.FloatField(default = 50)
    Cargofijo = models.FloatField(default = 60)
    def __unicode__(self):
        return '%s %s' % ((str(self.Mes)), str(self.Anio))

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
    Costo_kWh_verano= models.FloatField(default = 0)
    Costo_kWh_fverano= models.FloatField(default = 0)
    Anio = models.ForeignKey(Anio, blank=True, null=True)
    Mes = models.ForeignKey(Meses, blank=True, null=True)
    def __unicode__(self):
        return '%s %s %s' % (str(self.AreaCont), str(self.Mes), str(self.Anio))

