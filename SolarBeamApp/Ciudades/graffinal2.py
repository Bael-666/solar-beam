import PIL as pillow
from PIL import Image, ImageDraw, ImageFont

def main(tax):
    im3 = Image.new("RGB", (1500, 1800), (245,245,185,255)).convert('RGBA')
    im4 = Image.new("RGB", (1500, 1950), (245,245,185,255)).convert('RGBA')
    draw = ImageDraw.Draw(im3)
    fnt = ImageFont.truetype('app/static/font/Ubuntu-Bold.ttf', 60)
    e = ImageDraw.Draw(im3)
    meses = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']

    for m in range(12):
    	draw.polygon(((150,150*m),(300,125*m+150),(300,125*m+270),(150,150+150*m)),fill=(59,153,76,255))
        draw.rectangle(((0,150*m),(150,150*m+150)),fill=(76,193,96,255))
        e.text((20,m*150+40), meses[m], font=fnt, fill=(255,255,255,255))
    #draw.rectangle(((0,0),(5,1800)),fill=(245,245,185,255))
    #draw.rectangle(((0,0),(155,5)),fill=(245,245,185,255))
    #draw.rectangle(((0,1795),(155,1800)),fill=(245,245,185,255))
    mec = [0,0,0,0,0,0,0,0,0,0,0,0]
    graf = max(tax)

    for i in range(12):
        tax2 = (tax[i]/graf)*1190
        mec[i] = int(round(tax2))
        draw.rectangle(((300,125*i+150),(300+mec[i],125*i+270)),fill=(76,193,96,255))

    fnt = ImageFont.truetype('app/static/font/Ubuntu-Bold.ttf', 80)
    e = ImageDraw.Draw(im3)

    for n in range(12):
        data = str(round(tax[n],2))
        e.text((415,n*125+163), data+" kWh", font=fnt, fill=(255,255,255,255))
    im4.paste(im3,(0,75))
    im4.save("app/static/imagenes/grafica1.jpg")