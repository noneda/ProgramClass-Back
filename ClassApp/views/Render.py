from django.shortcuts import render

def Index (req):
    return render(
        request = req, template_name='index.html' , Sequence = {'pageName' : "Home"}
    )