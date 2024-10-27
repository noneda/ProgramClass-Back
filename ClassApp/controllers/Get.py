
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
def sendDataClass(req, name):
    ClassSelect = Class_Main.objects.get(title = name)
    ClassSelectConvert = Serializer_Class_Main(ClassSelect);
    
    ClassSection = Class_Section.objects.all().filter(Class = ClassSelect.id).order_by('Order')
    sendSection = []
    
    # * Get Class :# 
    for section in ClassSection:
        SubSection = Class_SubSection.objects.all().filter(Section = section.id).order_by('Order')
        Question = Class_Question.objects.all().filter(Section = section.id).order_by('Order')
        
        cls = []
        sub = []
        ask = []
        order = []
        for subsection in SubSection:
            serialize = Serializer_Class_SubSection(subsection)
            cls.append([serialize.data['Name'], serialize.data['Order']])
            sub.append([serialize.data['Name'], serialize.data['Order']])
            
        for question in Question:
            serialize = Serializer_Class_Question(question)
            cls.append([serialize.data['Name'], serialize.data['Order']])
            ask.append([serialize.data['Name'], serialize.data['Order']])

        save = 1
        s_index = 0
        a_index = 0

        while s_index < len(sub) or a_index < len(ask):
            if a_index < len(ask) and ask[a_index][1] == save:
                order.append(ask[a_index])
                save += 1
                a_index += 1
            elif s_index < len(sub) and sub[s_index][1] == save:
                order.append(sub[s_index])
                save += 1
                s_index += 1
            else:
                if a_index < len(ask):
                    a_index += 1
                if s_index < len(sub):
                    s_index += 1
                                
        convert = Serializer_Class_Section(section)
        sendSection.append({
            'id' : convert.data['id'],
            'Section' : convert.data['Name'],
            'Order' :  convert.data['Order'],
            'Class' : order
        })
        
        
    TestSend = {
        'id' : ClassSelectConvert.data['id'],
        "Class" : ClassSelectConvert.data['title'],
        "set" : sendSection, 
    }
    
    
    return JsonResponse(TestSend)


@api_view(['GET'])
def sendSection(req, id):
    Section = Class_Section.objects.get(id = id)
    ConvertSSection = Serializer_Class_Section(Section)
    SubSection = Class_SubQuestion.objects.all().filter(Section = Section.id).order_by('Order')
    
    
    pass