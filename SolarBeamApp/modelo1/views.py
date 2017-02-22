from django.shortcuts import render
from pulp import *
from .models import Demanda, Fabrica, Tienda, Whiskas
import whisky

def index(request):
    rutas = Demanda.objects.order_by('costo')
    fabricas = Fabrica.objects.order_by('produccion')
    tiendas = Tienda.objects.order_by('demand')
    #modelo = modelo.main(rutas, fabricas, tiendas)
    context = {'rutas': rutas}
    return render(request, 'modelo1/index.html', context)

def whiskas(request):
    whiska = Whiskas.objects.all()
    whisk = whisky.main(whiska)
    fob = value(whisk.objective)
    status = LpStatus[whisk.status]
    context = {'whiskas': whiska, 'whisk': whisk, 'fob': fob, 'status': status}
    return render(request, 'modelo1/whiskas.html', context)
