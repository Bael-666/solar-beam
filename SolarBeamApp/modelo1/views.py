from django.shortcuts import render
from pulp import *
import whisky, model
from .models import Demanda, Fabrica, Tienda, Whiskas


def index(request):
    rutas = Demanda.objects.all()
    fabricas = Fabrica.objects.all()
    tiendas = Tienda.objects.all()
    modelo = model.main(rutas, fabricas, tiendas)
    fob = value(modelo.objective)
    status = LpStatus[modelo.status]
    context = {'rutas': rutas, 'modelo': modelo, 'fob': fob, 'status': status}
    return render(request, 'modelo1/index.html', context)

def whiskas(request):
    whiska = Whiskas.objects.all()
    whisk = whisky.main(whiska)
    fob = value(whisk.objective)
    status = LpStatus[whisk.status]
    context = {'whiskas': whiska, 'whisk': whisk, 'fob': fob, 'status': status}
    return render(request, 'modelo1/whiskas.html', context)
