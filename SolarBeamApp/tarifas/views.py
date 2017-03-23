from django.shortcuts import get_object_or_404, render
from .models import Ciudades, DAC, Tarifa1x, Meses, Tarifa2, Anio, AreasControl
from datetime import datetime
import graf, tarf2ener, grafd

def index(request):
    context = {'year':datetime.now().year}
    return render(request, 'tarifas/index.html', context)

def tarifa1(request):
    ciudades = Ciudades.objects.all()
    context = {'ciudades':ciudades, 'year':datetime.now().year}
    return render(request, 'tarifas/tarifa1.html', context)

def detalles(request, ciudades_id):
    ciudad = get_object_or_404(Ciudades, pk=ciudades_id)
    tarifa = Tarifa1x.objects.filter(Nombre__startswith = ciudad.Tarifa+" -")
    context = {'ciudad':ciudad, 'tarifa':tarifa, 'year':datetime.now().year}
    return render(request, 'tarifas/detalles.html', context)

def tarifa2(request):
    tarifa2_historico = Tarifa2.objects.order_by('-Anio', 'Mes')
    mes = Meses.objects.all()
    anio = Anio.objects.all()
    graf.main(tarifa2_historico)
    context = {'year':datetime.now().year, 'hist':tarifa2_historico, 'meses': mes, 'anio': anio}
    return render(request, 'tarifas/tarifa2.html', context)

def t2energia(request):
    init = int(request.POST['init'])
    ulti = int(request.POST['ulti'])
    fact = float(request.POST['fact'])
    mes1 = get_object_or_404(Meses, pk=request.POST['mes1'])
    mes2 = get_object_or_404(Meses, pk=request.POST['mes2'])
    a = int(request.POST['mes1'])
    b = int(request.POST['mes2'])
    c = b - a
    if c > 1:
        mes3 =get_object_or_404(Meses, pk = a + 1)
        fact3 = Tarifa2.objects.filter(Anio = request.POST['anio'], Mes=mes3)
    else:
        mes3 = 0
        fact3 = 0
    fact1 = Tarifa2.objects.filter(Anio = request.POST['anio'], Mes=mes1)
    fact2 = Tarifa2.objects.filter(Anio = request.POST['anio'], Mes=mes2)
    cost, iva, total = tarf2ener.main(init, ulti, fact, mes1, mes2, fact1, fact2, mes3, fact3)
    context = {'cost': cost, 'iva': iva, 'total': total}
    return render(request, 'tarifas/t2energia.html', context)

def dac(request):
    Acont = AreasControl.objects.all()
    context = {'Acont': Acont}
    return render(request, 'tarifas/dac.html', context)

def dac2(request, areascontrol_id):
    acont = get_object_or_404(AreasControl, pk=areascontrol_id)
    dac = DAC.objects.filter(AreaCont= acont).order_by('-Anio', 'Mes')
    grafd.main(dac, acont)
    context = {'dac': dac, 'acont': acont}
    return render(request, 'tarifas/dac2.html', context)