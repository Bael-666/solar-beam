from django.shortcuts import render, get_object_or_404
from .models import Central, CentralOv, Centrales, Ofererc, Paqgen, Paquetes, Paquetes2, Nodoof, Regionof, Sistemainter, Zonaof, Paqin, Paqexc, Conpaqexc, Ofertas, Centrales_sim, Gen, Paqgen_sim
import SLP2017, convert, resul, getNodes, sim, lcen
from pulp import *
from datetime import datetime
import json
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Max

# Create your views here.
@login_required
def index(request):
    return render(request, 'SLP17/index.html')

def new_usr(request):
    return render(request, 'SLP17/new_usr.html')

def alta_usr(request):
    username = str(request.POST['email'])
    password = str(request.POST['password'])
    user = User.objects.create_user(username=username, email = username, password = password, is_staff = 0, is_active = 1, is_superuser = 0)
    user.save()
    return render(request, 'SLP17/alta_usr.html',{'user':user})

@login_required
def simulador(request):
    gen2 = int(request.user.id) + 500
    Gen.objects.get_or_create(gen = gen2)
    cent = Centrales_sim.objects.filter(gen = gen2)
    paq = Paqgen_sim.objects.filter(gen = gen2)
    cen2, paq2 = sim.main(cent, paq)
    context = {'cent':cen2, 'paq':paq2}
    return render(request, 'SLP17/simulador.html', context)

@login_required
def alta_paq1(request):
    gen2 = int(request.user.id) + 500
    cent = Centrales_sim.objects.filter(gen = gen2)
    context = {'cent':cent}
    return render(request, 'SLP17/alta_paq1.html', context)

@login_required
def alta_paq2(request):
    gen2 = int(request.user.id) + 500
    a = request.POST.getlist('checks')
    cent = Centrales_sim.objects.filter(pk__in = a)
    user = request.user
    gen2 = int(user.id) + 500
    a = Paqin_sim.objects.filter(gen = gen2).aggregate(Max('paquete'))

    
    if a['paquete__max']:
        cen2 = int(a['paquete__max'])+ 1
        cen = Centrales_sim(gen = gen2, central = cen2, nombre_cen = nombre_cen, prelacion = prelacion, capapl = capapl, zpcen = nodo.sistemainter, zgcen = nodo.zona, zprcen = nodo.region, zicen = nodo.nodo)
    else:
        cen = Centrales_sim(gen = gen2, central = 1, nombre_cen = nombre_cen, prelacion = prelacion, capapl = capapl, zpcen = nodo.sistemainter, zgcen = nodo.zona, zprcen = nodo.region, zicen = nodo.nodo)
    cen.save()
    return render(request, 'SLP17/alta_paq2.html')

@login_required
def alta_cen(request):
    regionof = Regionof.objects.order_by('nombrereg')
    context = {'regionof': regionof, 'year': datetime.now().year, 'title':'Primera Subasta de Largo Plazo 2015'}
    return render(request, 'SLP15/alta_cen.html', context)

@login_required
def alta_cen2(request):
    regionof = Regionof.objects.order_by('nombrereg')
    nodoof = Nodoof.objects.order_by('nombrenodo')
    region = get_object_or_404(regionof, pk=request.POST['region'])
    nodo = get_object_or_404(nodoof, pk=request.POST['nodo'])
    capapl = float(request.POST['capapl'])
    prelacion = int(request.POST['prelacion'])
    nombre_cen = str(request.POST['nombre_cen'])
    user = request.user
    gen2 = int(user.id) + 500
    a = Centrales_sim.objects.filter(gen = gen2).aggregate(Max('central'))
    if a['central__max']:
        cen2 = int(a['central__max'])+ 1
        cen = Centrales_sim(gen = gen2, central = cen2, nombre_cen = nombre_cen, prelacion = prelacion, capapl = capapl, zpcen = nodo.sistemainter, zgcen = nodo.zona, zprcen = nodo.region, zicen = nodo.nodo)
    else:
        cen = Centrales_sim(gen = gen2, central = 1, nombre_cen = nombre_cen, prelacion = prelacion, capapl = capapl, zpcen = nodo.sistemainter, zgcen = nodo.zona, zprcen = nodo.region, zicen = nodo.nodo)
    cen.save()
    return render(request, 'SLP17/alta_cen2.html')

@login_required
def resultados(request):
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
    slp2017, Up, Uc, DemP, DemC, DemE = SLP2015.main(paqgen, ofererc, central, centrales, centralov2, paqin2, paqexc2, paquetes, paquetes2, ofertas, conpaqexc, nodoof, regionof, zonaof, sistemainter)
    Upaq, Compra, Ucen = resul.main(paqgen, ofererc, centrales, Up, Uc, DemP, DemC, DemE)
    fob = value(slp2017.objective)
    status = LpStatus[slp2017.status]
    context = {'slp2017': slp2017, 'fob': fob, 'status': status, 'paqgen': paqgen, 'Up': Upaq, 'Uc': Ucen, 'Compra': Compra}
    return render(request, 'SLP17/resultados.html', context)

@login_required
def getNode(request):
    idRequest = request.body
    if request.is_ajax():
        jsonId = json.loads(idRequest)
        idRegion = jsonId['idRegion']
        result = getNodes.getNodes(idRegion)
        return HttpResponse(result)
    else:
        html = '<p>This is not ajax</p>'      
        return HttpResponse(html)

