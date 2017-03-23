from django.shortcuts import get_object_or_404, render
from Ciudades.models import Ciudade, Panele, Inversore
from tarifas.models import Meses
import principal,  inicial, inversor, final, graffinal2
from django.utils import timezone

def home(request):

    ciudades = Ciudade.objects.order_by('Estados')
    panel = Panele.objects.all()
    inver = Inversore.objects.all()
    context = {'ciudades': ciudades, 'panel': panel, 'inver': inver}
    return render(request, 'Ciudades/pruebas4.html',context)

def Solarbeam2(request):
    ciudades = Ciudade.objects.order_by('Estados')
    panel = Panele.objects.all()
    inver = Inversore.objects.all()
    context = {'ciudades': ciudades, 'panel': panel, 'inver': inver}
    return render(request, 'Ciudades/SB2index.html',context)

def resultados(request):
    ciudades = Ciudade.objects.order_by('Estados')
    Ciud = get_object_or_404(Ciudade, pk=request.POST['Ciudad'])
    panel = Panele.objects.get(pk = request.POST['Panel'])
    inver = Inversore.objects.get(pk = request.POST['Inversor'])
    per = int(request.POST['ener'])
    tipo = int(request.POST['tipo'])
    kwhanor = float(request.POST['demanda'])
    cab = float(request.POST['cable'])
    meses = Meses.objects.all()
    paneles = Panele.objects.all()
    inversores = Inversore.objects.all()
    kwhan = inicial.main(kwhanor, per)
    kwp, prom, incl, PerT, npan, valinc, hspmensual, kwhan1 = principal.main(Ciud, kwhan, cab, panel, tipo, meses, inver)
    ninver, conex = inversor.main(npan, panel, kwp, inver)
    tempmen, kwh, kwf, hsp, efsist, kwdia, ahorroaino, ahorrodosaino, arb1, arb2, kwhtot = final.main(PerT, kwp, valinc, inver, cab, hspmensual, npan, panel)
    graffinal2.main(kwh)
    hora = timezone.now()
    mes2 = zip(meses, tempmen, kwh)
    context = { 'arb1': arb1,'arb2': arb2,'ahorrodosaino':ahorrodosaino,'ahorroaino':ahorroaino,'kwdia':kwdia, 'efsist':efsist, 'hora':hora,'kwf':kwf,'per': per, 'kwhanor':kwhanor, 'ciudades': ciudades, 'hsp':hsp, 'kwh':kwh, 'Ciud': Ciud, 'kwhan': kwhtot, 'kwp':kwp, 'prom': prom, 'incl': incl, 'mes2':mes2, 'npan':npan, 'panel':panel, 'conex':conex, 'tipo':tipo, 'paneles': paneles, 'inversores': inversores, 'ninver': ninver, 'inver' : inver}
    return render(request, 'Ciudades/pruebas3.html', context)

def resumen(request):
    ciudades = Ciudade.objects.order_by('Estados')
    Ciud = get_object_or_404(Ciudade, pk=request.POST['Ciudad'])
    panel = Panele.objects.get(pk = request.POST['Panel'])
    inver = Inversore.objects.get(pk = request.POST['Inversor'])
    per = int(request.POST['ener'])
    tipo = int(request.POST['tipo'])
    kwhanor = float(request.POST['demanda'])
    cab = float(request.POST['cable'])
    meses = Meses.objects.all()
    paneles = Panele.objects.all()
    inversores = Inversore.objects.all()
    kwhan = inicial.main(kwhanor, per)
    kwp, prom, incl, PerT, npan, valinc, hspmensual, kwhan1 = principal.main(Ciud, kwhan, cab, panel, tipo, meses, inver)
    ninver, conex = inversor.main(npan, panel, kwp, inver)
    tempmen, kwh, kwf, hsp, efsist, kwdia, ahorroaino, ahorrodosaino, arb1, arb2, kwhtot = final.main(PerT, kwp, valinc, inver, cab, hspmensual, npan, panel)
    graffinal2.main(kwh)
    hora = timezone.now()
    mes2 = zip(meses, tempmen, kwh)
    potint = float(ninver*inver.MaxPowAC)/1000
    invpot = float(inver.MaxPowAC)/1000
    context = { 'arb1': arb1,'arb2': arb2,'ahorrodosaino':ahorrodosaino,'ahorroaino':ahorroaino,'kwdia':kwdia, 'efsist':efsist, 'hora':hora,'kwf':kwf,'per': per, 'kwhanor':kwhanor, 'ciudades': ciudades, 'hsp':hsp, 'kwh':kwh, 'Ciud': Ciud, 'kwhan': kwhtot, 'kwp':kwp, 'prom': prom, 'incl': incl, 'mes2':mes2, 'npan':npan, 'panel':panel, 'conex':conex, 'tipo':tipo, 'paneles': paneles, 'inversores': inversores, 'ninver': ninver, 'inver' : inver, 'potint': potint, 'invpot': invpot}
    return render(request, 'Ciudades/resumen2.html', context)
