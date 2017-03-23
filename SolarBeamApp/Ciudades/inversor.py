from Ciudades.models import Inversore
import math

def micro(kwp,panel, npan, inv):
    ninver = math.ceil(kwp/inv.MaxPow)
    if npan <= 12:
        panserf = npan
    else:
        panserf = 12
    vocf = panserf*panel.Voc
    vmppf = panserf*panel.Vmpp
    iscf = panel.Isc
    imppf = panel.Impp
    paralelof = math.ceil(npan/12)
    posalf = (ninver*inv.MaxPowAC)/1000
    return ninver, panserf, vocf, vmppf, iscf, imppf, inv, paralelof, posalf

def invcen(kwp, panel, npan, inv):
    ninver = int(math.ceil(kwp/inv.MaxPow))
    conex = []
    for i in range(ninver):
        mpan = npan
        if i > 0:
            for j in conex:
                mpan = mpan - j[0]*j[1]

        panser = 0
        panpar = 0
        while panser*panel.Voc < inv.MPPM and panser < mpan and (panser+1)*panel.Wp < inv.MaxPow :
            panser = panser + 1
        while panser*(panpar + 1) <= mpan and (panpar + 1)*panel.Impp < inv.MaxDC and panser*(panpar + 1)*panel.Wp < inv.MaxPow:
            panpar = panpar + 1
        conex.append([panser, panpar])
    for i in range(ninver):
        pot = int(panel.Wp*conex[i][0]*conex[i][1])
        voc = panel.Voc*conex[i][0]
        vmpp = panel.Vmpp*conex[i][0]
        isc = panel.Isc*conex[i][1]
        impp = panel.Impp*conex[i][1]
        conex[i].append(pot) 
        conex[i].append(voc)
        conex[i].append(vmpp) 
        conex[i].append(isc)
        conex[i].append(impp)
    return conex, ninver
    

def main(npan,panel,kwp, inver):
    if inver.Tipo == 'MI':
        ninver, panser, voc, vmpp, isc, impp, inversor, paralelo, potsal = micro(kwp, panel, npan, inver)
        conex = [panser, paralelo, potsal, voc, vmpp, isc, impp]
    else:
        conex, ninver = invcen(kwp, panel, npan, inver)
    return ninver, conex