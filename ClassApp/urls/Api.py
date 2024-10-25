from django.urls import path 
from ..controllers.Get import * 

urlpatterns = [
    path(route = '', view = getData, name= "ApiHomePage")
]