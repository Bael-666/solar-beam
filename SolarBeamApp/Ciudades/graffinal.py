from PIL import Image, ImageDraw, ImageFont

def main(tax):
    im1 = Image.open("/home/Shirohige/SolarBeam/Ciudades/static/imagenes/meses2.jpg")
    im2 = Image.open("/home/Shirohige/SolarBeam/Ciudades/static/imagenes/ver12.jpg")
    im3 = Image.new("RGB", (1500, 1800), "white").convert('RGBA')
    im4 = Image.new("RGB", (1200, 1500), "white").convert('RGBA')

    mec = [0,0,0,0,0,0,0,0,0,0,0,0]
    graf = max(tax)

    for i in range(12):
	    tax2 = (tax[i]/graf)*1200
	    mec[i] = int(round(tax2))
    for j in range(12):
        for k in range(mec[j]):
            im4.paste(im2,(k,j*125,k+1,j*125+125))

    fnt = ImageFont.truetype('/home/Shirohige/SolarBeam/Ciudades/static/font/Ubuntu-Bold.ttf', 80)
    e = ImageDraw.Draw(im4)

    for n in range(12):
        data = str(round(tax[n],2))
        e.text((115,n*125+8), data+" kWh", font=fnt, fill=(255,255,255,255))
    im4.save("/home/Shirohige/SolarBeam/Ciudades/static/imagenes/graf5.jpg")
    im3.paste(im1,(0,0,150,1800))
    im3.paste(im4,(300,150,1500,1650))
    im3.save("/home/Shirohige/SolarBeam/Ciudades/static/imagenes/grafica1.jpg")
