from django.contrib import admin

# Register your models here.
from .models import Fabrica, Tienda, Demanda, Whiskas

admin.site.register(Fabrica)
admin.site.register(Tienda)
admin.site.register(Demanda)
admin.site.register(Whiskas)