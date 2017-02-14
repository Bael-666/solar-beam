from django.contrib import admin

# Register your models here.
from .models import Fabrica, Tienda, Demanda

admin.site.register(Fabrica)
admin.site.register(Tienda)
admin.site.register(Demanda)