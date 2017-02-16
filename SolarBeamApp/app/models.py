"""
Definition of models.
"""

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Anexo2Centrales(models.Model):
    nombre_cen = models.TextField(db_column='NOMBRE_CEN')  # Field name made lowercase.
    central = models.IntegerField(db_column='CENTRAL')  # Field name made lowercase.
    capapl = models.IntegerField(db_column='CAPAPL')  # Field name made lowercase.
    zpcen = models.IntegerField(db_column='ZPCEN')  # Field name made lowercase.
    zgcen = models.IntegerField(db_column='ZGCEN')  # Field name made lowercase.
    zprcen = models.IntegerField(db_column='ZPRCEN')  # Field name made lowercase.
    zicen = models.IntegerField(db_column='ZICEN')  # Field name made lowercase.
    gen = models.IntegerField(db_column='GEN')  # Field name made lowercase.
    prelacion = models.IntegerField(db_column='PRELACION')  # Field name made lowercase.
    cent_acept = models.IntegerField(db_column='CENT_ACEPT', blank=True, null=True)  # Field name made lowercase.
    factorp = models.DecimalField(db_column='FACTORP', max_digits=10, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANEXO_2_CENTRALES'


class Anexo2CentralOv(models.Model):
    gen = models.IntegerField(db_column='GEN')  # Field name made lowercase.
    paquetes = models.IntegerField(db_column='PAQUETES')  # Field name made lowercase.
    central = models.IntegerField(db_column='CENTRAL')  # Field name made lowercase.
    porceea = models.DecimalField(db_column='PORCEEA', max_digits=10, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANEXO_2_CENTRAL_OV'


class Anexo2Confzgen(models.Model):
    gen = models.IntegerField(db_column='GEN')  # Field name made lowercase.
    rinpre = models.IntegerField(db_column='RINPRE')  # Field name made lowercase.
    nodin = models.IntegerField(db_column='NODIN')  # Field name made lowercase.
    paquetes = models.IntegerField(db_column='PAQUETES')  # Field name made lowercase.
    sinterc = models.IntegerField(db_column='SINTERC')  # Field name made lowercase.
    zongen = models.IntegerField(db_column='ZONGEN')  # Field name made lowercase.
    zprecio = models.IntegerField(db_column='ZPRECIO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANEXO_2_CONFZGEN'


class Anexo2Factordesesp(models.Model):
    factorprefpesos = models.DecimalField(db_column='FACTORPREFPESOS', max_digits=10, decimal_places=8)  # Field name made lowercase.
    porciondlsnominal = models.DecimalField(db_column='PORCIONDLSNOMINAL', max_digits=10, decimal_places=8)  # Field name made lowercase.
    porciondlsreal = models.DecimalField(db_column='PORCIONDLSREAL', max_digits=10, decimal_places=8)  # Field name made lowercase.
    porcionpesosrealid = models.DecimalField(db_column='PORCIONPESOSREALID', max_digits=10, decimal_places=8)  # Field name made lowercase.
    tasadevesp = models.DecimalField(db_column='TASADEVESP', max_digits=10, decimal_places=8)  # Field name made lowercase.
    porcionpesosnominal = models.DecimalField(db_column='PORCIONPESOSNOMINAL', max_digits=10, decimal_places=8)  # Field name made lowercase.
    porcionpesosrealip = models.DecimalField(db_column='PORCIONPESOSREALIP', max_digits=10, decimal_places=8)  # Field name made lowercase.
    tasabonos = models.DecimalField(db_column='TASABONOS', max_digits=10, decimal_places=8)  # Field name made lowercase.
    tasabonosusd = models.DecimalField(db_column='TASABONOSUSD', max_digits=10, decimal_places=8)  # Field name made lowercase.
    tasaembi = models.DecimalField(db_column='TASAEMBI', max_digits=10, decimal_places=8)  # Field name made lowercase.
    tasaudibono = models.DecimalField(db_column='TASAUDIBONO', max_digits=10, decimal_places=8)  # Field name made lowercase.
    tasatips = models.DecimalField(db_column='TASATIPS', max_digits=10, decimal_places=8)  # Field name made lowercase.
    p = models.IntegerField(db_column='P')  # Field name made lowercase.
    e = models.IntegerField(db_column='E')  # Field name made lowercase.
    c = models.IntegerField(db_column='C')  # Field name made lowercase.
    i = models.DecimalField(db_column='I', max_digits=10, decimal_places=8)  # Field name made lowercase.
    iden = models.DecimalField(db_column='ID', max_digits=10, decimal_places=8)  # Field name made lowercase.
    t = models.DecimalField(db_column='T', max_digits=10, decimal_places=8)  # Field name made lowercase.
    umbral_sener = models.DecimalField(db_column='UMBRAL_SENER', max_digits=10, decimal_places=8)  # Field name made lowercase.
    tcusd = models.DecimalField(db_column='TCUSD', max_digits=10, decimal_places=8)  # Field name made lowercase.
    usd_compra = models.DecimalField(db_column='USD_COMPRA', max_digits=10, decimal_places=8)  # Field name made lowercase.
    vpnusda = models.DecimalField(db_column='VPNUSDA', max_digits=10, decimal_places=8)  # Field name made lowercase.
    vpnusdb = models.DecimalField(db_column='VPNUSDB', max_digits=10, decimal_places=8)  # Field name made lowercase.
    vpnmxna = models.DecimalField(db_column='VPNMXNA', max_digits=10, decimal_places=8)  # Field name made lowercase.
    vpnmxnb = models.DecimalField(db_column='VPNMXNB', max_digits=10, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANEXO_2_FACTORDESESP'


class Anexo2Ofererc(models.Model):
    dpot = models.FloatField(db_column='DPOT', blank=True, null=True)  # Field name made lowercase.
    ppot = models.FloatField(db_column='PPOT', blank=True, null=True)  # Field name made lowercase.
    deea = models.IntegerField(db_column='DEEA', blank=True, null=True)  # Field name made lowercase.
    peea = models.IntegerField(db_column='PEEA', blank=True, null=True)  # Field name made lowercase.
    dcel = models.IntegerField(db_column='DCEL', blank=True, null=True)  # Field name made lowercase.
    pcel = models.IntegerField(db_column='PCEL', blank=True, null=True)  # Field name made lowercase.
    fechairrantp = models.IntegerField(db_column='FECHAIRRANTP', blank=True, null=True)  # Field name made lowercase.
    fechairrdespp = models.IntegerField(db_column='FECHAIRRDESPP', blank=True, null=True)  # Field name made lowercase.
    fechairrante = models.IntegerField(db_column='FECHAIRRANTE', blank=True, null=True)  # Field name made lowercase.
    fechairrdespe = models.IntegerField(db_column='FECHAIRRDESPE', blank=True, null=True)  # Field name made lowercase.
    fechairrantc = models.IntegerField(db_column='FECHAIRRANTC', blank=True, null=True)  # Field name made lowercase.
    fechairrdespc = models.IntegerField(db_column='FECHAIRRDESPC', blank=True, null=True)  # Field name made lowercase.
    erc = models.IntegerField(db_column='ERC', blank=True, null=True)  # Field name made lowercase.
    ofertas = models.IntegerField(db_column='OFERTAS', blank=True, null=True)  # Field name made lowercase.
    zpoterc = models.IntegerField(db_column='ZPOTERC', blank=True, null=True)  # Field name made lowercase.
    sinterc = models.IntegerField(db_column='SINTERC', blank=True, null=True)  # Field name made lowercase.
    rinerc = models.IntegerField(db_column='RINERC', blank=True, null=True)  # Field name made lowercase.
    potajus = models.IntegerField(db_column='POTAJUS', blank=True, null=True)  # Field name made lowercase.
    eeaajus = models.IntegerField(db_column='EEAAJUS', blank=True, null=True)  # Field name made lowercase.
    celajus = models.IntegerField(db_column='CELAJUS', blank=True, null=True)  # Field name made lowercase.
    ejecucion = models.TextField(db_column='EJECUCION', blank=True, null=True)  # Field name made lowercase.
    ppotajus = models.FloatField(db_column='PPOTAJUS', blank=True, null=True)  # Field name made lowercase.
    peeaajus = models.IntegerField(db_column='PEEAAJUS', blank=True, null=True)  # Field name made lowercase.
    pcelajus = models.IntegerField(db_column='PCELAJUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANEXO_2_OFERERC'


class Anexo2Paqexc(models.Model):
    gen = models.IntegerField(db_column='GEN', blank=True, null=True)  # Field name made lowercase.
    conpaqexc = models.IntegerField(db_column='CONPAQEXC', blank=True, null=True)  # Field name made lowercase.
    paquetes = models.IntegerField(db_column='PAQUETES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANEXO_2_PAQEXC'


class Anexo2Paqin(models.Model):
    gen = models.IntegerField(db_column='GEN', blank=True, null=True)  # Field name made lowercase.
    paquetes = models.IntegerField(db_column='PAQUETES', blank=True, null=True)  # Field name made lowercase.
    paquetes2 = models.IntegerField(db_column='PAQUETES2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANEXO_2_PAQIN'


class Anexo2Regionof(models.Model):
    sistemainter = models.IntegerField(db_column='SISTEMAINTER', blank=True, null=True)  # Field name made lowercase.
    zona = models.IntegerField(db_column='ZONA', blank=True, null=True)  # Field name made lowercase.
    region = models.IntegerField(db_column='REGION', blank=True, null=True)  # Field name made lowercase.
    nombrereg = models.TextField(db_column='NOMBREREG', blank=True, null=True)  # Field name made lowercase.
    limene = models.IntegerField(db_column='LIMENE', blank=True, null=True)  # Field name made lowercase.
    iden = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANEXO_2_REGIONOF'


class Anexo2Sistemainter(models.Model):
    sistemainter = models.IntegerField(db_column='SISTEMAINTER', blank=True, null=True)  # Field name made lowercase.
    nombresi = models.TextField(db_column='NOMBRESI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANEXO_2_SISTEMAINTER'


class Anexo2Zonaof(models.Model):
    zona = models.IntegerField(db_column='ZONA', blank=True, null=True)  # Field name made lowercase.
    sistemainter = models.IntegerField(db_column='SISTEMAINTER', blank=True, null=True)  # Field name made lowercase.
    nombrezon = models.TextField(db_column='NOMBREZON', blank=True, null=True)  # Field name made lowercase.
    limeeae = models.IntegerField(db_column='LIMEEAE', blank=True, null=True)  # Field name made lowercase.
    iden = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANEXO_2_ZONAOF'


class Anexo2Zprecio(models.Model):
    iden = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    pml = models.FloatField(db_column='PML', blank=True, null=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='NOMBRE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANEXO_2_ZPRECIO'


class Anexo2Paqgen(models.Model):
    paquetes = models.IntegerField(db_column='PAQUETES', blank=True, null=True)  # Field name made lowercase.
    gen = models.IntegerField(db_column='GEN', blank=True, null=True)  # Field name made lowercase.
    gpot = models.IntegerField(db_column='GPOT', blank=True, null=True)  # Field name made lowercase.
    geea = models.FloatField(db_column='GEEA', blank=True, null=True)  # Field name made lowercase.
    gcel = models.IntegerField(db_column='GCEL', blank=True, null=True)  # Field name made lowercase.
    ppaq = models.FloatField(db_column='PPAQ', blank=True, null=True)  # Field name made lowercase.
    firrant = models.IntegerField(db_column='FIRRANT', blank=True, null=True)  # Field name made lowercase.
    firrdes = models.IntegerField(db_column='FIRRDES', blank=True, null=True)  # Field name made lowercase.
    sint = models.IntegerField(db_column='SINT', blank=True, null=True)  # Field name made lowercase.
    zonin = models.IntegerField(db_column='ZONIN', blank=True, null=True)  # Field name made lowercase.
    rin = models.IntegerField(db_column='RIN', blank=True, null=True)  # Field name made lowercase.
    nin = models.IntegerField(db_column='NIN', blank=True, null=True)  # Field name made lowercase.
    prelacion = models.IntegerField(db_column='PRELACION', blank=True, null=True)  # Field name made lowercase.
    factordevesp = models.FloatField(db_column='FACTORDEVESP', blank=True, null=True)  # Field name made lowercase.
    pct20 = models.IntegerField(db_column='PCT20', blank=True, null=True)  # Field name made lowercase.
    vpnindexdls = models.FloatField(db_column='VPNINDEXDLS', blank=True, null=True)  # Field name made lowercase.
    vpnindexpesos = models.FloatField(db_column='VPNINDEXPESOS', blank=True, null=True)  # Field name made lowercase.
    indexusd = models.IntegerField(db_column='INDEXUSD', blank=True, null=True)  # Field name made lowercase.
    idejec = models.IntegerField(db_column='IDEJEC', blank=True, null=True)  # Field name made lowercase.
    nppaq = models.FloatField(db_column='NPPAQ', blank=True, null=True)  # Field name made lowercase.
    ev_ppajus = models.IntegerField(db_column='EV_PPAJUS', blank=True, null=True)  # Field name made lowercase.
    ev_pporig = models.IntegerField(db_column='EV_PPORIG', blank=True, null=True)  # Field name made lowercase.
    aceptado = models.TextField(db_column='ACEPTADO', blank=True, null=True)  # Field name made lowercase.
    zongenf = models.TextField(db_column='ZONGENF', blank=True, null=True)  # Field name made lowercase.
    fechaap = models.TextField(db_column='FECHAAP', blank=True, null=True)  # Field name made lowercase.
    fechaen = models.TextField(db_column='FECHAEN', blank=True, null=True)  # Field name made lowercase.
    zprecio = models.IntegerField(db_column='ZPRECIO', blank=True, null=True)  # Field name made lowercase.
    prioridad = models.IntegerField(db_column='PRIORIDAD', blank=True, null=True)  # Field name made lowercase.
    ev_pp10 = models.IntegerField(db_column='EV_PP10', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANEXO_2_paqgen'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'



