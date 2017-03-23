from PIL import Image, ImageDraw, ImageFont

def main(tax):

    im = Image.open("/home/Shirohige/SolarBeam/Ciudades/static/imagenes/img3.jpg")
    im2 = Image.new("RGB", (500, 900), "white").convert('RGBA')
    im3 = Image.open("/home/Shirohige/SolarBeam/Ciudades/static/imagenes/img4.jpg")

    ima = Image.open("/home/Shirohige/SolarBeam/Ciudades/static/imagenes/cuadro1.jpg")
    ima2 = Image.open("/home/Shirohige/SolarBeam/Ciudades/static/imagenes/cuadro2.jpg")
    ima3 = Image.new("RGB", (200, 1200), "white").convert('RGBA')

    imf = Image.new("RGB", (800, 1200), "white").convert('RGBA')

    mec = [0,0,0,0,0,0,0,0,0,0,0,0]
    graf = max(tax)

    for i in range(12):
    	tax2 = (tax[i]/graf)*500
    	mec[i] = int(round(tax2))
    for j in range(12):
	    for k in range(mec[j]):
		    if j % 2 == 0:
			    im2.paste(im,(k,j*75,k+1,j*75+75))
            else:
	    		im2.paste(im3,(k,j*75,k+1,j*75+75))

# make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', im2.size, (255,255,255,0))
    txt2 = Image.new('RGBA', ima3.size, (255,255,255,0))

# get a font
    fnt = ImageFont.truetype('/home/Shirohige/SolarBeam/Ciudades/static/font/Ubuntu-Regular.ttf', 44)
    fnt2 = ImageFont.truetype('/home/Shirohige/SolarBeam/Ciudades/static/font/Ubuntu-Regular.ttf', 40)
# get a drawing context
    d = ImageDraw.Draw(txt)
    e = ImageDraw.Draw(txt2)

# draw text, half opacity
    d.text((20,10), "Enero", font=fnt, fill=(255,255,255,255))
# draw text, full opacity
    d.text((20,85), "Febrero", font=fnt, fill=(255,255,255,255))
    d.text((20,160), "Marzo", font=fnt, fill=(255,255,255,255))
    d.text((20,235), "Abril", font=fnt, fill=(255,255,255,255))
    d.text((20,310), "Mayo", font=fnt, fill=(255,255,255,255))
    d.text((20,385), "Junio", font=fnt, fill=(255,255,255,255))
    d.text((20,460), "Julio", font=fnt, fill=(255,255,255,255))
    d.text((20,535), "Agosto", font=fnt, fill=(255,255,255,255))
    d.text((20,610), "Septiembre", font=fnt, fill=(255,255,255,255))
    d.text((20,685), "Octubre", font=fnt, fill=(255,255,255,255))
    d.text((20,760), "Noviembre", font=fnt, fill=(255,255,255,255))
    d.text((20,835), "Diciembre", font=fnt, fill=(255,255,255,255))

    out1 = Image.alpha_composite(im2, txt)
    out1.save("/home/Shirohige/SolarBeam/Ciudades/static/imagenes/imagen.jpg")

    for i in range(12):
    	if i % 2 == 0:
    		ima3.paste(ima,(0,i*100,100,i*100+100))
	    	ima3.paste(ima,(100,i*100,200,i*100+100))
        else:
	    	ima3.paste(ima2,(0,i*100,100,i*100+100))
	    	ima3.paste(ima2,(100,i*100,200,i*100+100))
        data = str(tax[i])
        e.text((10,i*100+25), data+"kWh", font=fnt2, fill=(255,255,255,255))

    out2 = Image.alpha_composite(ima3, txt2)
    out2.save("/home/Shirohige/SolarBeam/Ciudades/static/imagenes/imagen2.jpg")
    imf.paste(out2,(0,0,200,1200))
    imf.paste(out1,(200,150,700,1050))
    imf.save("/home/Shirohige/SolarBeam/Ciudades/static/imagenes/graf.jpg")

