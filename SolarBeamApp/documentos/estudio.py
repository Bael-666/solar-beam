import time
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from io import BytesIO
def std1(response):
    buffer = BytesIO()
    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly.
    p.showPage()
    p.save()
    c = canvas.Canvas("hello.pdf")
    c.drawString(100,750,"Welcome to Reportlab!")
    c.save()
    s = canvas.Canvas('hola.pdf', pagesize=letter)
    width, height = letter
    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    s.drawString(100,750,"Welcome to Reportlab!")
    s.save()
    response.write(pdf)
    return response
def std2(response, d3, d6):
    a = canvas.Canvas(response, pagesize=letter)
    a.setLineWidth(.3)
    a.setFont('Helvetica', 12)
    a.drawString(30,750,'OFFICIAL COMMUNIQUE')
    a.drawString(30,735,'OF ACME INDUSTRIES')
    a.drawString(500,750,"12/12/2010")
    a.line(480,747,580,747)
    a.drawString(275,725,'AMOUNT OWED:')
    a.drawString(500,725,"$1,000.00")
    a.line(378,723,580,723)
    a.drawString(30,703, str(d3))
    a.line(120,700,580,700)
    a.drawString(120,703,str(d6))
 
    a.save()
    return response

def std3(response, d3, d6):   
    doc = SimpleDocTemplate(response,pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
    Story=[]
    logo = "app/static/tarifas/plot.png"
    magName = "Pythonista"
    issueNum = 12
    subPrice = "99.00"
    limitedDate = "03/05/2010"
    freeGift = "tin foil hat"
    formatted_time = time.ctime()
    full_name = "Mike Driscoll"
    address_parts = ["411 State St.", "Marshalltown, IA 50158"]
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    ptext = '<font size=20>%s</font>' % d6
    Story.append(Paragraph(ptext, styles["Normal"]))  
    Story.append(Spacer(1, 12))
    im = Image(logo, 5*inch, 4*inch)
    Story.append(im)
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '<font size=12>%s</font>' % formatted_time
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
 
# Create return address
    ptext = '<font size=12>%s</font>' % full_name
    Story.append(Paragraph(ptext, styles["Normal"]))       
    for part in address_parts:
        ptext = '<font size=12>%s</font>' % part.strip()
        Story.append(Paragraph(ptext, styles["Normal"]))   
 
    Story.append(Spacer(1, 12))
    ptext = '<font size=12>Dear %s:</font>' % full_name.split()[0].strip()
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
 
    ptext = '<font size=12>We would like to welcome you to our subscriber base for %s Magazine! \
            You will receive %s issues at the excellent introductory price of $%s. Please respond by\
            %s to start receiving your subscription and get the following free gift: %s.</font>' % (magName, 
                                                                                                issueNum,
                                                                                                subPrice,
                                                                                                limitedDate,
                                                                                                freeGift)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
 
 
    ptext = '<font size=12>Thank you very much and we look forward to serving you.</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size=12>Sincerely,</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 48))
    ptext = '<font size=12>Ima Sucker</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    doc.build(Story)
    return response