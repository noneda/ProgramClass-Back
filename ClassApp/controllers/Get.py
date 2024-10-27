
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from ..models import *
from ..serializers import *


@api_view(['GET'])
def getData(req):
    send = {
        'name': "Api about ClassApp",
        'author': "noneda",
        'version': "1.0.0",
    }
    return JsonResponse(send)

@api_view(['GET'])
def sendAllClass(req):
    obj = Class_Main.objects.all()
    convert = Serializer_Class_Main(obj, many = True)
    message  = "Not Have Errors :#"
    if not obj:
        message = "Dont Found! Anything"
    send = {
        "Message" : message,
        "Data" : convert.data 
    }
    return JsonResponse(send)
    

@api_view(['GET'])
def sendUniqueData(req, id):
    obj = Class_Main.objects.get(id = id)
    convert = Serializer_Class_Main(obj)
    message  = "Not Have Errors :#"
    if not obj:
        message = "Dont Found! Anything"
    send = {
        "Message" : message,
        "Data" : convert.data 
    }
    return JsonResponse(send)