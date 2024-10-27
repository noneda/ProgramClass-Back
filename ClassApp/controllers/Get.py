
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


@api_view(['GET'])
def sendDataClass(req, id):
    ClassSelect = Class_Main.objects.get(id = id)
    ClassSelectConvert = Serializer_Class_Main(ClassSelect);
    
    ClassSection = Class_Section.objects.all().filter(Class = ClassSelect.id).order_by('Order')
    sendSection = []
    
    # * Get Class :# 
    for section in ClassSection:
        SubSection = Class_SubSection.objects.all().filter(Section = section.id).order_by('Order')
        Question = Class_Question.objects.all().filter(Section = section.id).order_by('Order')
        sendSubSection = []
        for subsection in SubSection:
            SubConvert = Serializer_Class_SubSection(subsection)
            sendSubSection.append({
                'Order' : SubConvert.data['Order'],
                'Name' : SubConvert.data['Name']
            })
        for question in Question:
            QuestConvert = Serializer_Class_Question(question)
            sendSubSection.append(QuestConvert.data)
            
        SecConvert = Serializer_Class_Section(section)
        sendSection.append([SecConvert.data, sendSubSection])
    
    #TODO: Order Sections
    
    
    TestSend = {
        "Class" : ClassSelectConvert.data,
        "Sections" : sendSection, 
    }
    
    
    return JsonResponse(TestSend)