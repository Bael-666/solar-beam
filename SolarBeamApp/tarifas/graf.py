import numpy as np
import matplotlib.pyplot as plt

def main(datos):
    m = []
    a = []
    b = []
    n = []
    c = []
    fig = plt.figure()
    cont = 0
    plt.rc('font',family='Gotham bold')
    for i in datos:
        m.append(cont)
        n.append(str(i.Mes)+" "+str(i.Anio))
        a.append(i.Basico)
        b.append(i.Inter)
        c.append(i.Excedente)
        cont = cont + 1
    d = ['Ene 2014', 'Jul 2014', 'Ene 2015', 'Jul 2015', 'Ene 2016', 'May 2016', 'Mar 2017']
    e = [0, 6, 12, 18, 24, 28, 38]
    plt.xticks(e, d, rotation = 45, fontsize = '9')
    plt.yticks( fontsize = '9')
    plt.plot(m, a, m, b, m, c) 
    plt.plot(m[28:], a[28:],'red', linewidth=3.0)
    plt.plot(m[28:], b[28:],'red', linewidth=3.0)
    plt.plot(m[28:], c[28:],'red', linewidth=3.0)
     
    plt.title('Incremento del costo en Tarifa 2', fontsize = '11')
    plt.grid(True)
    plt.ylabel("Pesos por kWh", fontsize = '8')
    plt.legend(['Costo de 0 a 50 kWh consumidos en el mes','Costo de 51 a 100 kWh consumidos en el mes','Costo de 101 > kWh consumidos en el mes'], loc='upper left', fontsize = '9')
    plt.tight_layout()
    fig.savefig('app/static/tarifas/tarifa2_hist.png')
