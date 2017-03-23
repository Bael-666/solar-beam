from __future__ import unicode_literals

from django.db import models

class Inversore(models.Model):
    Marca = models.CharField(max_length=30)
    Modelo = models.CharField(max_length=15)
    def __unicode__(self):
        return self.Modelo
    MinPow = models.IntegerField()
    MaxPow = models.IntegerField()
    MaxPowAC = models.IntegerField()
    MPPL = models.IntegerField()
    MPPM = models.IntegerField()
    MinV = models.IntegerField()
    MaxDC = models.FloatField()
    MEfc240 = models.FloatField()
    MEfc208 = models.FloatField()
    A240 = models.FloatField()
    A208 = models.FloatField()
    MA240 = models.FloatField()
    MA208 = models.FloatField()
    Tipo_opciones = (
        ('MI', 'Microinversor'),
        ('IC', 'Inversor Central'),
    )
    Tipo = models.CharField(max_length=2,
                                    choices=Tipo_opciones,
                                    default='IC')



class Panele(models.Model):
    Marca = models.CharField(max_length=30)
    Modelo = models.CharField(max_length=15)
    def __unicode__(self):
        return self.Modelo
    Wp = models.IntegerField()
    Largo = models.IntegerField()
    Ancho = models.IntegerField()
    Peso = models.FloatField()
    Voc = models.FloatField()
    Vmpp = models.FloatField()
    Isc = models.FloatField()
    Impp = models.FloatField()
    PTC = models.FloatField()

class Ciudade(models.Model):
    Nombre = models.CharField(max_length=30)
    def __unicode__(self):
        return self.Nombre

    Estados_Opciones = (
        ('AG', 'Aguascalientes'),
        ('BC', 'Baja California'),
        ('BS', 'Baja California Sur'),
        ('Ca', 'Campeche'),
        ('Cp', 'Chiapas'),
        ('Ch', 'Chihuahua'),
        ('Cu', 'Coahuila'),
        ('Co', 'Colima'),
        ('DF', 'Distrito Federal'),
        ('Du', 'Durango'),
        ('EM', 'Estado de Mexico'),
        ('Gt', 'Guanajuato'),
        ('Gr', 'Guerrero'),
        ('Hd', 'Hidalgo'),
        ('Ja', 'Jalisco'),
        ('Mi', 'Michoacan'),
        ('Mo', 'Morelos'),
        ('Na', 'Nayarit'),
        ('NL', 'Nuevo Leon'),
        ('Oa', 'Oaxaca'),
        ('Pu', 'Puebla'),
        ('Qt', 'Queretaro'),
        ('QR', 'Quintana Roo'),
        ('SL', 'San Luis Potosi'),
        ('Si', 'Sinaloa'),
        ('So', 'Sonora'),
        ('Ta', 'Tabasco'),
        ('Tm', 'Tamaulipas'),
        ('Tl', 'Tlaxcala'),
        ('Ve', 'Veracruz'),
        ('Yu', 'Yucatan'),
        ('Za', 'Zacatecas'),
    )
    Estados = models.CharField(max_length=2,
                                      choices=Estados_Opciones,
                                      default='AG')
    Latitud = models.FloatField()
    HSP_Ene = models.FloatField()
    HSP_Feb = models.FloatField()
    HSP_Mar = models.FloatField()
    HSP_Abr = models.FloatField()
    HSP_May = models.FloatField()
    HSP_Jun = models.FloatField()
    HSP_Jul = models.FloatField()
    HSP_Ago = models.FloatField()
    HSP_Sep = models.FloatField()
    HSP_Oct = models.FloatField()
    HSP_Nov = models.FloatField()
    HSP_Dic = models.FloatField()
    Temp_Ene = models.FloatField()
    Temp_Feb = models.FloatField()
    Temp_Mar = models.FloatField()
    Temp_Abr = models.FloatField()
    Temp_May = models.FloatField()
    Temp_Jun = models.FloatField()
    Temp_Jul = models.FloatField()
    Temp_Ago = models.FloatField()
    Temp_Sep = models.FloatField()
    Temp_Oct = models.FloatField()
    Temp_Nov = models.FloatField()
    Temp_Dic = models.FloatField()

# Create your models here.
