import numpy as np
import matplotlib.pyplot as plt

def main(datos, area):
    m = []
    a = []
    b = []
    n = []
    c = []
    fig = plt.figure()
    cont = 0
    for i in datos:
        m.append(cont)
        n.append(str(i.Mes)+" "+str(i.Anio))
        a.append(i.Costo_kWh_verano)
        b.append(i.Costo_kWh_fverano)
        cont = cont + 1
    d = ['Ene 2014', 'Jul 2014', 'Ene 2015', 'Jul 2015', 'Ene 2016', 'May 2016', 'Mar 2017']
    e = [0, 6, 12, 18, 24, 28, 38]
    plt.xticks(e, d, rotation = 45)
    plt.plot(m, a, m, b ) 
    plt.plot(m[28:], a[28:],'red', linewidth=3.0)
    plt.plot(m[28:], b[28:],'red', linewidth=3.0)
    plt.title('Incremento del costo en la Tarifa de Alto Consumo')
    plt.grid(True)
    plt.ylabel("Pesos por kWh")
    plt.legend(['Tarifa de Verano','Tarifa fuera de verano'], loc='upper left')
    plt.tight_layout()
    fig.savefig('app/static/tarifas/tarifadac_'+str(area.AreasControl)+'.png')
