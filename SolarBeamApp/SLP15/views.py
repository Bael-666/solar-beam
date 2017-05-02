from django.shortcuts import render
from .models import Central, CentralOv, Centrales, Ofererc, Paqgen, Paquetes, Paquetes2, Nodoof, Regionof, Sistemainter, Zonaof, Paqin, Paqexc, Conpaqexc, Ofertas, Centrales_sim, Gen, Paqgen_sim
import SLP2015, convert, resul, getNodes
from pulp import *
from datetime import datetime
import json
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
    return render(request, 'SLP15/index.html')

def new_usr(request):
    return render(request, 'SLP15/new_usr.html')

def alta_usr(request):
    username = str(request.POST['email'])
    password = str(request.POST['password'])
    user = User.objects.create_user(username=username, email = username, password = password, is_staff = 0, is_active = 1, is_superuser = 0)
    user.save()
    return render(request, 'SLP15/alta_usr.html',{'user':user})

@login_required
def simulador(request):
    gen2 = int(request.user.id) + 500
    Gen.objects.get_or_create(gen = gen2)
    try:
        cent = Centrales_sim.objects.get(gen = gen2)
    except Centrales_sim.DoesNotExist:
        a = "No hay centrales dadas de alta"
    try:
        paq = Paqgen_sim.objects.get(gen = gen2)
    except Paqgen_sim.DoesNotExist:
        b = "No hay ofertas dadas de alta"
    if a and b:
        context = {'a':a, 'b': b}
    elif a:
        context = {'paq':paq, 'a':a}
    elif b:
        context = {'cent':cent, 'b': b}
    else:
        context = {'cent':cent, 'paq':paq}
    return render(request, 'SLP15/simulador.html', context)

@login_required
def alta_cen(request):
    regionof = Regionof.objects.order_by('nombrereg')
    context = {'regionof': regionof, 'year': datetime.now().year, 'title':'Primera Subasta de Largo Plazo 2015'}
    return render(request, 'SLP15/alta_cen.html', context)

@login_required
def alta(request):
    regionof = Regionof.objects.order_by('nombrereg')
    region = get_object_or_404(regionof, pk=request.POST['region'])
    nodo = get_object_or_404(nodoof, pk=request.POST['nodo'])
    capapl = float(request.POST['capapl'])
    prelacion = int(request.POST['prelacion'])
    nombre_cen = str(request.POST['nombre_cen'])
    user = request.user
    gen2 = int(user.id) + 500
    cen = Centrales_sim(gen = gen2, central = 1, nombre_cen = nombre_cen, prelacion = prelacion, capapl = capapl, zpcen = nodo.sistemainter, zgcen = nodo.zona, zprcen = nodo.region, zncen = nodo.nodo)
    cen.save()
    cen.delete()
    return render(request, 'SLP15/alta.html')

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
    slp2015, Up, Uc, DemP, DemC, DemE = SLP2015.main(paqgen, ofererc, central, centrales, centralov2, paqin2, paqexc2, paquetes, paquetes2, ofertas, conpaqexc, nodoof, regionof, zonaof, sistemainter)
    Upaq, Compra, Ucen = resul.main(paqgen, ofererc, centrales, Up, Uc, DemP, DemC, DemE)
    fob = value(slp2015.objective)
    status = LpStatus[slp2015.status]
    context = {'slp2015': slp2015, 'fob': fob, 'status': status, 'paqgen': paqgen, 'Up': Upaq, 'Uc': Ucen, 'Compra': Compra}
    return render(request, 'SLP15/resultados.html', context)

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

