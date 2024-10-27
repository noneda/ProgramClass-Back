from django.shortcuts import render
from ..forms import *

def Index (req):
    return render(
        req, 'index.html', {'pageName' : "Home"}
    )
    
def viewFormMain (req):
    form = Class_Main_Form(req.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        'pageName' : "Class Main",
        'form' : form
    };
    
    return render(req, 'form.html', context)

def viewFormSection (req):
    form = Class_Section_Form(req.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
         'pageName' : "Class Section",
         'form' : form
    }
    
    return render(
        req, 'form.html', context
    )

def viewFormSubSection (req):
    form = Class_SubSection_Form(req.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
         'pageName' : "Class Section",
         'form' : form
    }
    
    return render(
        req, 'form.html', context
    )


def viewFormQuestion(req):
    form = Class_Question_Form(req.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
         'pageName' : "Class Section",
         'form' : form
    }
    
    return render(
        req, 'form.html', context
    )
