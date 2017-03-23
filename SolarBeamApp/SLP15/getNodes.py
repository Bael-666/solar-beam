from .models import Nodoof, Regionof
from django.core import serializers
import json

def getNodes(idRegion):
    data = []
    r = Regionof.objects.values('sistemainter', 'zona', 'region').get(id = idRegion)
    n = Nodoof.objects.filter(sistemainter = r['sistemainter'], zona = r['zona'], region = r['region']).values('id', 'nombrenodo')
    for i in n:
        data.append(i)
    data = json.dumps(data)
    return data
