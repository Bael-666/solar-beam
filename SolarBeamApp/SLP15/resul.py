def main(paqgen, ofererc, centrales, Up, Uc, DemP, DemC, DemE):
    Upaq = []
    Compra = []
    Ucen = []
    
    for i in paqgen:
 #       if Up[i].value() == 1:
            x1 = int(i.id)
            x2 = int(Up[i].value())
            x3 = int(i.gen)
            x4 = int(i.paquetes)
            x5 = z = int(i.aceptado)
            Upaq.append([x1, x2, x5, x3, x4]) 
    for i in ofererc:
        y1 = int(i.id)
        y5 = int(i.erc)
        y6 = int(i.ofertas)
        y2 = DemP[i].value()
        y3 = DemE[i].value()
        y4 = DemC[i].value()
        Compra.append([y1, y5, y6, y2, float(i.potajus), y3, float(i.eeaajus), y4, float(i.celajus)])

    for i in centrales:  
        z1 = int(i.id)
        z2 = Uc[i].value()
        z3 = int(i.gen)
        z4 = int(i.central)
        try:
            z5 = int(i.cent_acept)  
        except ValueError:
            pass
        Ucen.append([z1, z2, z5, z3, z4]) 
    return Upaq, Compra, Ucen
