from Ciudades.models import Inversore
import math


def main(npan,panel,kwp, ciudad):
    if npan < 7:
        inversor = Inversore.objects.get(MaxPow = 250)
        ninver = math.ceil(kwp/inversor.MaxPow)
        panser = npan
        voc = npan*panel.Voc
        vmpp = npan*panel.Vmpp
        isc = panel.Isc
        impp = panel.Impp
    if kwp >= 1500 and kwp <= 6000 :
        inversor = Inversore.objects.get(MinPow__lte = kwp, MaxPow__gte = kwp)
        for i in inversor():
            panser = math.floor(i.MPPM/panel.Voc)
            voc = npan*panel.Voc
            vmpp = npan*panel.Vmpp
            isc = panel.Isc
            impp = panel.Impp
    if kwp <= 8000 and kwp > 6000:
        kwptemp = kwp/2
        ninver = 2
        inversor = Inversore.objects.get(MinPow__lte = kwptemp, MaxPow__gte = kwptemp)
        panser = math.floor(inversor.MPPM/panel.Voc)
    if kwp <= 12000 and kwp > 8000:
        kwptemp = kwp/2
        ninver = 2
        inversor = Inversore.objects.get(MinPow__lte = kwptemp, MaxPow__gte = kwptemp)
        panser = math.floor(inversor.MPPM/panel.Voc)
    if kwp <= 18000 and kwp > 12000:
        kwptemp = kwp/3
        ninver = 3
        inversor = Inversore.objects.get(MinPow__lte = kwptemp, MaxPow__gte = kwptemp)
        panser = math.floor(inversor.MPPM/panel.Voc)
    if npan <= panser:
        panpar = 1
        panser = npan
        voc = npan*panel.Voc
        vmpp = npan*panel.Vmpp
        isc = panel.Isc
        impp = panel.Impp

    elif npan%2 == 0:
        panpar = 2
        panser = npan/2
        voc = panser*panel.Voc
        vmpp = panser*panel.Vmpp
        isc = panpar*panel.Isc
        impp = panpar*panel.Impp

    elif npan%3 == 0:
        panpar = 3
        panser = npan/3
        voc = panser*panel.Voc
        vmpp = panser*panel.Vmpp
        isc = panpar*panel.Isc
        impp = panpar*panel.Impp
    return inversor, panser, panpar,voc,vmpp,isc,impp, ninver

