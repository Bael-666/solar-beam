def main(paqin, paqexc, centralov, centrales, paqgen):
    paqin2 = []
    paqexc2 = []
    centralov2 = []
    for i in paqin:
        x = 0
        y = 0
        for j in paqgen:
            if i.gen == j.gen and i.paquetes == j.paquetes and x == 0:
                x = j
            if i.gen == j.gen and i.paquetes2 == j.paquetes and y == 0:
                y = j
        if x != 0 and y != 0:
            paqin2.append((x,y))
    for i in paqexc:
        x = 0
        y = 0
        for j in paqgen:
            if i.gen == j.gen and i.paquetes == j.paquetes:
                x = j
        y = i.conpaqexc
        if x != 0:
            paqexc2.append((y,x))

    for i in centralov:
        x = 0
        y = 0
        for j in paqgen:
            if i.gen == j.gen and i.paquetes == j.paquetes:
                x = j
        for k in centrales:
            if i.gen == k.gen and i.central == k.central:
                y = k
        if x != 0 and y != 0:        
            centralov2.append((x,y))
    return paqin2, paqexc2, centralov2
