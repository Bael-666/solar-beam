# coding=utf-8
#[15,17,20,23,20,18,15,14,13,17,17,15]
def main(perdid, porp, meses): #Temperatura media y porcentaje de perdida

	mes = []
	for i in range(12):
	    temp = perdid[i]+(1.25*(45-20))
	    mes.append(1 - (porp*(temp - 25)))

	return mes
