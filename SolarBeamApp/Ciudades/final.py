def main(PerT, kwp, valinc, inversor, cab, hspmensual, npan, panel):
    kwh = [0,0,0,0,0,0,0,0,0,0,0,0]
    tempmen = [0,0,0,0,0,0,0,0,0,0,0,0]
    hsp = 0
    eftemp = 0
    for i in range(12):
        eftemp = PerT[i] + eftemp
        tempmen[i] = PerT[i]*kwp*.001
        kwh[i] = (kwp*valinc[i]*PerT[i]*inversor.MEfc208*hspmensual[i]*cab)/1000
        hsp = kwh[i] + hsp
    prom_eftemp = eftemp/12
    efsist = prom_eftemp*cab*inversor.MEfc208*100
    kwf = kwp/1000
    kwdia = hsp/365
    ahorroaino = hsp*3.80
    ahorrodosaino = ahorroaino*25
    arb1 = hsp*.65*25
    arb2 = arb1/500
    arb1 = arb1/1000
    kwhtot = sum(kwh)
    return tempmen, kwh, kwf, hsp,efsist, kwdia, ahorroaino, ahorrodosaino, arb1, arb2, kwhtot