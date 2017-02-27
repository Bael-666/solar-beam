# Import PuLP modeler functions
from pulp import *

def main(paqgen, ofererc, central, centrales, centralov, paqin, paqexc, paquetes, paquetes2, ofertas, conpaqexc, nodoof, regionof, zonaof, sistemainter):
    # Create the 'prob' variable to contain the problem data
    prob = LpProblem("Subasta de Largo Plazo 2015", LpMaximize)
    # A dictionary called 'ingredient_vars' is created to contain the referenced Variables
    Up = LpVariable.dicts("Paquetes", paqgen, cat = LpBinary)
    Uc = LpVariable.dicts("Centrales", centrales, cat = LpBinary)
    DemP = LpVariable.dicts("Compra Potencia", ofererc, lowBound = 0, cat = LpContinuous)
    DemE = LpVariable.dicts("Compra Energia", ofererc, lowBound = 0,cat = LpContinuous)
    DemC = LpVariable.dicts("Compra Cel", ofererc, lowBound = 0,cat = LpContinuous)
    # TFuncion objetivo
    prob += lpSum([i.ppot*DemP[i] for i in ofererc]) + lpSum([n.peea*DemE[n] for n in ofererc])  + lpSum([m.pcel*DemC[m] for m in ofererc]) - lpSum([Up[j]*j.nppaq for j in paqgen]), "Maximo excedente economico"

    # 1 Restriccion de compra de potencia
    for i in sistemainter:
        prob += lpSum([j.gpot*Up[j] for j in paqgen 
                                        if i.sistemainter == j.sint]) >= lpSum([DemP[k] for k in ofererc
                                                                                 if i.sistemainter == k.sinterc])
    # 2 Restriccion de compra de potencia por sistema interconectado en fecha irregular anterior                                                                                      
    for i in sistemainter:
        prob += lpSum([j.gpot*Up[j]*j.firrant for j in paqgen 
                                                   if i.sistemainter == j.sint]) <= lpSum([DemP[k]*k.fechairrantp for k in ofererc 
                                                                                          if i.sistemainter == k.sinterc])
    # 3 Restriccion de compra de potencia por sistema interconectado en fecha irregular anterior
    for i in sistemainter:
        prob += lpSum([j.gpot*Up[j]*j.firrdes for j in paqgen 
                                        if i.sistemainter == j.sint]) <= lpSum([DemP[k]*k.fechairrdespp for k in ofererc 
                                                                          if i.sistemainter == k.sinterc])

    # 4 restriccion de compra de energia electrica acumulable
    prob += lpSum([j.geea*Up[j] for j in paqgen]) >= lpSum([DemE[k] for k in ofererc]), "EEA %s"%j

    # 5 restriccion de compra de certificados de energia limpia
    prob += lpSum([j.gcel*Up[j] for j in paqgen]) >= lpSum([DemC[k] for k in ofererc]), "CEL %s"%j

    # 6 restriccion de compra de certificados de energia limpia en fecha irregular anterior
    prob += lpSum([j.gcel*Up[j]*j.firrant for j in paqgen]) <= lpSum([DemC[k]*k.fechairrantc for k in ofererc]), "CEL fecha irregular anterior %s"%j

    # 7 restriccion de compra de certificados de energia limpia en fecha irregular posterior
    prob += lpSum([j.gcel*Up[j]*j.firrdes for j in paqgen]) <= lpSum([DemC[k]*k.fechairrantc for k in ofererc]), "CEL fecha irregular posterior %s"%j
    
    # 8 restriccion de compra de Potencia
    for j in ofererc:
         prob += DemP[j] <= j.dpot

    # 9 restriccion de compra de EEA
    for j in ofererc:
        prob += DemE[j] <= j.deea

    # 10 restriccion de compra de CEL
    for j in ofererc:
        prob += DemC[j] <= j.dcel

    # 11 OFERTAS CONDICIONADAS
    print paqgen
    print Up
    for i in paqin:
        prob += Up[i[0]] <= Up[i[1]]

    # 12 OFERTAS CONDICIONADAS
    for i in conpaqexc:
        prob += lpSum([Up[j[1]] for j in paqexc
                                            if j[0] == i.conpaqexc]) <= 1
    # 13 Centrales Aceptadas y paquetes aceptados
    for i in centralov:
        prob += Up[i[0]] <= Uc[i[1]]
    
    # 14 Limite de potencia puntos de interconexion
    for i in nodoof:
        prob += lpSum([Uc[j]*j.prelacion*j.capapl for j in centrales
                                          if i.sistemainter == j.zpcen and i.zona == j.zgcen and i.region == j.zprcen and i.nodo == j.zicen])  <= i.limpotn

    # 15 Limite de potencia puntos de interconexion
    for i in regionof:
        prob += lpSum([Uc[j]*j.prelacion*j.capapl for j in centrales
                                          if i.sistemainter == j.zpcen and i.zona == j.zgcen and i.region == j.zprcen])  <= i.limpot

    # 16 Limite de potencia puntos de interconexion
    for i in zonaof:
        prob += lpSum([Up[j]*j.prelacion*j.geea for j in paqgen
                                          if i.sistemainter == j.sint and i.zona == j.zonin])  <= i.limeeae
    #The problem is solved using PuLP's choice of Solver
    prob.solve()
    return prob