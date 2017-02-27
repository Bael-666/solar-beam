from django.shortcuts import render
from .models import Central, CentralOv, Centrales, Ofererc, Paqgen, Paquetes, Paquetes2, Nodoof, Regionof, Sistemainter, Zonaof, Paqin, Paqexc, Conpaqexc, Ofertas 
import SLP2015, convert
from pulp import *
# Create your views here.

def index(request):
    central = Central.objects.all()
    centralov = CentralOv.objects.all()
    centrales = Centrales.objects.all()
    ofererc = Ofererc.objects.all()
    paqgen = Paqgen.objects.all()
    paquetes = Paquetes.objects.all()
    paquetes2 = Paquetes2.objects.all()
    nodoof = Nodoof.objects.all()
    regionof = Regionof.objects.all()
    sistemainter = Sistemainter.objects.all()
    zonaof = Zonaof.objects.all()
    paqin = Paqin.objects.all()
    paqexc = Paqexc.objects.all()
    conpaqexc = Conpaqexc.objects.all()
    ofertas = Ofertas.objects.all()
    paqin2, paqexc2, centralov2 = convert.main(paqin, paqexc, centralov, centrales, paqgen)
    slp2015 = SLP2015.main(paqgen, ofererc, central, centrales, centralov2, paqin2, paqexc2, paquetes, paquetes2, ofertas, conpaqexc, nodoof, regionof, zonaof, sistemainter)
    fob = value(slp2015.objective)
    status = LpStatus[slp2015.status]
    context = {'slp2015': slp2015, 'fob': fob, 'status': status, 'paqgen': paqgen}
    return render(request, 'SLP15/index.html', context)
# Create your views here.
