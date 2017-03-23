
def main(init, ulti, fact, mes1, mes2, fact1, fact2, mes3, fact3):
    a = mes1.Dias - init
    td = a + ulti
    if mes3 == 0:
        if a > ulti:
            if fact <= fact1.CBasico:
                costo = fact1.Cargofijo + fact*fact1.Basico
            elif fact <= 100 and fact > 50:
                costo = fact1.Cargofijo + (fact-50)*fact1.Inter + 50*fact1.Basico
            else:
                costo = fact1.Cargofijo + (fact-100)*fact1.Excedente + 50*fact1.Inter + 50*fact1.Basico
        else:
            if fact <= fact2.CBasico:
                costo = fact2.Cargofijo + fact*fact2.Basico
            elif fact <= 100 and fact > 50:
                costo = fact2.Cargofijo + (fact-50)*fact2.Inter + 50*fact1.Basico
            else:
                costo = fact2.Cargofijo + (fact-100)*fact2.Excedente + 50*fact2.Inter + 50*fact2.Basico
    else:
        if fact <= fact3[0].CBasico:
            costo = 2*fact3[0].Cargofijo + fact*fact3[0].Basico
        elif fact <= 100 and fact > 50:
            costo = 2*fact3[0].Cargofijo + (fact-100)*fact3[0].Inter + 100*fact3[0].Basico
        else:
            costo = 2*fact3[0].Cargofijo + (fact-200)*fact3[0].Excedente + 100*fact3[0].Inter + 100*fact3[0].Basico
#    for fact1 in facts1:
#        if c1 <= fact1.CBasico:
#            costo1 = p1*fact1.Cargofijo + c1*fact1.Basico
#        elif c1 <= 100 and c1 > 50:
#            costo1 = p1*fact1.Cargofijo + c1*fact1.Inter + 50*fact1.Basico
#        else:
#            costo1 = p1*fact1.Cargofijo + c1*fact1.Excedente + 50*fact1.Inter + 50*fact1.Basico
#    for fact2 in facts2:  
#        if c2 <= fact2.CBasico:
#            costo2 = p2*fact2.Cargofijo + c2*fact2.Basico
#        elif c2 <= 100 and c2 > 50:
#            costo2 = p2*fact2.Cargofijo + c2*fact2.Inter + 50*fact2.Basico
#        else:
#            costo2 = p2*fact2.Cargofijo + c2*fact2.Excedente + 50*fact2.Inter + 50*fact2.Basico
    iva = 0.16*costo
    total = costo + iva
    return costo, iva, total