import inc
# coding=utf-8
#[15,17,20,23,20,18,15,14,13,17,17,15]
def main(hspkw,hspmensual, lat, temp, diasmes, tipinc):
    lati = int(round(lat,0))
    incf = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
    incf = inc.main(lati)
    hspinc = [0,0,0,0,0,0,0]
    for i in range (7):
		for j in range (12):
		    hspinc[i] = hspmensual[i]*incf[i][j] + hspinc[i]
    hspi = max(hspinc)
    n = hspinc.index(hspi)
    if tipinc == 1:
	    lat = lat - 10
	    n = n - 2
	    valinc = incf[n]
    elif tipinc == 2:
	    lat = lat + 10
	    n = n + 2
	    valinc = incf[n]
    else:
        valinc = incf[n]
    return lat, valinc
