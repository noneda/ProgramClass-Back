
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.response import Response



@api_view(['GET'])
def getData(req):
    send = {
        'name': "Api about ClassApp",
        'author': "noneda",
        'version': "1.0.0",
    }
    return JsonResponse(send)