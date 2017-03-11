from django.shortcuts import get_object_or_404, render
from .models import Ciudades, DAC, Tarifa1x, Meses 
from datetime import datetime

def index(request):
    ciudades = Ciudades.objects.all()
    context = {'ciudades':ciudades}
    return render(request, 'tarifas/index.html', context)

def detalles(request, ciudades_id):
    ciudad = get_object_or_404(Ciudades, pk=ciudades_id)
    tarifa = Tarifa1x.objects.filter(Nombre__startswith = ciudad.Tarifa+" -")
    context = {'ciudad':ciudad, 'tarifa':tarifa}
    return render(request, 'tarifas/detalles.html', context)