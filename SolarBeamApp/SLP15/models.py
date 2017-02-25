from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
#@python_2_unicode_compatible
class Central(models.Model):
    central = models.IntegerField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    def __str__(self):
        return str(self.id)
#@python_2_unicode_compatible
class Centrales(models.Model):
    nombre_cen = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    central = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    capapl = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    zpcen = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    zgcen = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    zprcen = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    zicen = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    gen = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    prelacion = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    zpcen2 = models.TextField(blank=True, null=True)  # Field name made lowercase.
    zgcen2 = models.TextField(blank=True, null=True)  # Field name made lowercase.
    zprcen2 = models.TextField(blank=True, null=True)  # Field name made lowercase.
    zicen2 = models.TextField(blank=True, null=True)  # Field name made lowercase.
    cent_acept = models.TextField(max_length=1, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.id)
#@python_2_unicode_compatible
class Gen(models.Model):
    gen = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return str(self.id)
#@python_2_unicode_compatible
class Erc(models.Model):
    erc = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return str(self.id)
#@python_2_unicode_compatible
class CentralOv(models.Model):
    gen = models.ForeignKey(Gen)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    paquetes = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    central = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.id)
#@python_2_unicode_compatible
class Conpaqexc(models.Model):
    conpaqexc = models.IntegerField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    def __str__(self):
        return str(self.id)
#@python_2_unicode_compatible
class Nodoof(models.Model):
    sistemainter = models.IntegerField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    zona = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    region = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    nodo = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    limpotn = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    nombrenodo = models.TextField(blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.id)
#@python_2_unicode_compatible
class Ofererc(models.Model):
    dpot = models.IntegerField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    ppot = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    deea = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    peea = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    dcel = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    pcel = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    fechairrantp = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    fechairrdespp = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    fechairrante = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    fechairrdespe = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    fechairrantc = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    fechairrdespc = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    erc = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    ofertas = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    zpoterc = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    sinterc = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    rinerc = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    potajus = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    eeaajus = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    celajus = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    ejecucion = models.BigIntegerField(blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.id)

#@python_2_unicode_compatible
class Ofertas(models.Model):
    ofertas = models.IntegerField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    def __str__(self):
        return str(self.id)

#@python_2_unicode_compatible
class Paqexc(models.Model):
    gen = models.IntegerField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    conpaqexc = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    paquetes = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.id)

#@python_2_unicode_compatible
class Paqgen(models.Model):
    paquetes = models.IntegerField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    gen = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    capapl = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    gpot = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    geea = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    gcel = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    ppaq = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    firrant = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    firrdes = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    sint = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    zonin = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    rin = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    nin = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    prelacion = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    factordevesp = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    pct20 = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    vpnindexdls = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    vpnindexpesos = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    indexusd = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    idejec = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    nppaq = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    ev_ppajus = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    ev_pporig = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    aceptado = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    nin2 = models.BigIntegerField(blank=True, null=True)  # Field name made lowercase.
    rin2 = models.BigIntegerField(blank=True, null=True)  # Field name made lowercase.
    zonin2 = models.BigIntegerField(blank=True, null=True)  # Field name made lowercase.
    sint2 = models.BigIntegerField(blank=True, null=True)  # Field name made lowercase.
    zongenf = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    fechaap = models.TextField(blank=True, null=True)  # Field name made lowercase.
    fechaen = models.TextField(blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.id)
#@python_2_unicode_compatible
class Paqin(models.Model):
    gen = models.IntegerField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    paquetes = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    paquetes2 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.id)

#@python_2_unicode_compatible
class Paquetes(models.Model):
    paquetes = models.IntegerField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    def __str__(self):
        return str(self.id)

#@python_2_unicode_compatible
class Paquetes2(models.Model):
    paquetes2 = models.IntegerField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    def __str__(self):
        return str(self.id)

#@python_2_unicode_compatible
class Regionof(models.Model):
    sistemainter = models.IntegerField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    zona = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    region = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    nombrereg = models.TextField(blank=True, null=True)  # Field name made lowercase.
    limpot = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    pml = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    id_region = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.id)

#@python_2_unicode_compatible
class Sistemainter(models.Model):
    sistemainter = models.IntegerField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    nombresi = models.TextField(blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.id)
#@python_2_unicode_compatible
class Zonaof(models.Model):
    zona = models.IntegerField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    sistemainter = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    nombrezon = models.TextField(blank=True, null=True)  # Field name made lowercase.
    limpote = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    limeeae = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.id)