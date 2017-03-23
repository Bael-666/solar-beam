from django.contrib import admin

# Register your models here.
from .models import Ciudade, Inversore, Panele
admin.site.register(Ciudade)
admin.site.register(Inversore)
admin.site.register(Panele)