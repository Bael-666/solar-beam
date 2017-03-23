from django.shortcuts import render
from reportlab.pdfgen import canvas
from django.http import HttpResponse
import estudio

# Create your views here.
def index(request):
    return render(request, 'documentos/index.html')

def estudio1(request):
    return render(request, 'documentos/estudio1.html')

def genestudio1(request):
    d1 = float(request.POST['d1'])
    d2 = float(request.POST['d2'])
    d3 = float(request.POST['d3'])
    d4 = float(request.POST['d4'])
    d5 = float(request.POST['d5'])
    d6 = str(request.POST['d6'])
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="prueba.pdf"'
    response = estudio.std3(response, d3, d6)
    return response