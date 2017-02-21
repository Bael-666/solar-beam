from django.shortcuts import render

from .models import Demanda, Fabrica, Tienda


def index(request):
    rutas = Demanda.objects.order_by('costo')
    fabricas = Fabrica.objects.order_by('produccion')
    tiendas = Tienda.objects.order_by('demand')
    #modelo = modelo.main(rutas, fabricas, tiendas)
    context = {'rutas': rutas}
    return render(request, 'modelo1/index.html', context)

