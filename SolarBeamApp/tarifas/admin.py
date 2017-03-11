from django.contrib import admin

# Register your models here.
from .models import Tarifa1x, Temporada, Estados, Ciudades, AreasControl, Meses, DAC

admin.site.register(Tarifa1x)
admin.site.register(Temporada)
admin.site.register(Meses)
admin.site.register(DAC)
admin.site.register(Estados)
admin.site.register(Ciudades)
admin.site.register(AreasControl)
