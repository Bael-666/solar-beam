def main(paqin, paqexc, centralov, centrales, paqgen):
    paqin = []
    paqexc = []
    centralov = []
    for i in paqin:
        for j in paqgen:
            if i.gen == j.gen and i.paquetes == j.paquetes:
                x = j.id
            if i.gen == j.gen and i.paquetes2 == j.paquetes:
                y = j.id
        paqin.append((x,y))
    for i in paqexc:
        for j in paqgen:
            if i.gen == j.gen and i.paquetes == j.paquetes:
                x = j.id
        y = i.conpaqexc
        paqexc.append((y,x))

    for i in centralov:
        for j in paqgen:
            if i.gen == j.gen and i.paquetes == j.paquetes:
                x = j.id
        for k in centrales:
            if i.gen == k.gen and i.central == k.paquetes:
                y = j.id
        centralov.append((x,y))
    return paqin, paqexc, centralov
