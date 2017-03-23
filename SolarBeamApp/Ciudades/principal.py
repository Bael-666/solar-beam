#!/usr/bin/python
# coding=utf-8

import inclinacion, math, perdida

def main(Ciud,kWhAn, efcable, panel, tipinc, meses, inversor):
    hsp = 0
    diasmes = []
    for i in meses:
        diasmes.append(i.Dias)
    hspmensual = [0,0,0,0,0,0,0,0,0,0,0,0]
    hspkw = [Ciud.HSP_Ene, Ciud.HSP_Feb, Ciud.HSP_Mar, Ciud.HSP_Abr, Ciud.HSP_May, Ciud.HSP_Jun, Ciud.HSP_Jul, Ciud.HSP_Ago, Ciud.HSP_Sep, Ciud.HSP_Oct, Ciud.HSP_Nov, Ciud.HSP_Dic]
    TempM = [Ciud.Temp_Ene, Ciud.Temp_Feb, Ciud.Temp_Mar, Ciud.Temp_Abr, Ciud.Temp_May, Ciud.Temp_Jun, Ciud.Temp_Jul, Ciud.Temp_Ago, Ciud.Temp_Sep, Ciud.Temp_Oct, Ciud.Temp_Nov, Ciud.Temp_Dic]
    PerT = perdida.main(TempM, panel.PTC, meses)
    for i in range (12):
	    hspmensual[i] = diasmes[i]*hspkw[i] #HSP mensuales
    incli, valinc = inclinacion.main(hspkw, hspmensual, Ciud.Latitud, PerT, diasmes, tipinc)
    for i in range (12):
	    hsp = hsp + PerT[i]*hspmensual[i]*valinc[i]   #HSP con las perdidas por temperatura
    kWhAn = kWhAn/(inversor.MEfc208*efcable)
    kwp = kWhAn/hsp         
    prom = kWhAn/12                         #promedio de generación mensual
    npan = math.ceil((1000*kwp)/panel.Wp) #Numero de paneles
    kwpr = npan*panel.Wp              # Capacidad del sistema
    return kwpr, prom, incli, PerT, npan, valinc,hspmensual, kWhAn