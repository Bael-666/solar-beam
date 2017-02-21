from django.shortcuts import render

from .models import Demanda, Fabrica, Tienda, Whiskas


def index(request):
    rutas = Demanda.objects.order_by('costo')
    fabricas = Fabrica.objects.order_by('produccion')
    tiendas = Tienda.objects.order_by('demand')
    #modelo = modelo.main(rutas, fabricas, tiendas)
    context = {'rutas': rutas}
    return render(request, 'modelo1/index.html', context)

def whiskas(request):
    whiskas = Whiskas.objects.order_by('cost')
    #whisk = whisk.main(whikas)
    context = {'whiskas': whiskas}
    return render(request, 'modelo1/whiskas.html', context)
