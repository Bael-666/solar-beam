def main(cent):
    cen2 = []
    if cent:
        for i in cent:
            x1 = int(i.central)
            x2 = str(i.nombre_cen)
            x4 = int(i.capapl)
            x3 = int(i.id)
            cen2.append([x1, x2, x4, x3]) 
    return cen2