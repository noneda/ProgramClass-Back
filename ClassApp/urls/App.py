from django.urls import path 
from ..views.Render import *

urlpatterns = [
    path(route = '', view = Index, name= "AppHomePage")
]