from django.shortcuts import render
from ..forms import *
from ..models import *

def Index (req):
    return render(
        req, 'index.html', {'pageName' : "Home"}
    )
    
def viewFormMain (req):
    pageName =  "Class Main"
    Form = Class_Main_Form
    Data = Class_Main.objects.all()
    context = {
        'pageName' : pageName,
        'Form' : Form,
        'Data' : Data
    };
    
    if req.method == 'POST':
        form = Class_Main_Form(req.POST)
        form.save(commit=False)
        
        return render(req, 'form.html', context)
    else:
        return render(req, 'form.html', context)

def viewFormSection (req):
    return render(
        req, 'form.html', {
            'pageName' : "Class Section"
        }
    )

def viewFormSubSection (req):
    return render(
        req, 'form.html', {
            'pageName' : "Class SubSection"
        }
    )

def viewFormQuestion(req):
    return render(
        req, 'form.html', {
            'pageName' : "Class Question"
        }
    )