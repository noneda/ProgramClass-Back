from django.urls import path 
from ..views.Render import *

urlpatterns = [
    path(route = '', view = Index, name= "AppHomePage"),
    path(route='Class/', view=viewFormMain, name="Post Class Page"),
    path(route='Section/', view=viewFormSection, name="Post SubSection Page"),
    path(route='SubSection/', view=viewFormSubSection, name="Post Section Page"),
    path(route='Question/', view=viewFormQuestion, name="Post Question Page")
]