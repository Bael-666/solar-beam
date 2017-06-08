def main(cent, paq):
    cen2 = []
    paq2 = []
    if cent:
        for i in cent:
            x1 = int(i.central)
            x2 = str(i.nombre_cen)
            x4 = int(i.capapl)
            cen2.append([x1, x2, x4]) 
    if paq:
        for i in paq:
            x1 = int(i.paquetes)
            x2 = float(i.gpot)
            x4 = int(i.capapl)
            paq2.append([x1, x2, x4]) 
    return cen2, paq2