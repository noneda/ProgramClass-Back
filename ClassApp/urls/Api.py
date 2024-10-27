from django.urls import path 
from ..controllers.Get import * 

urlpatterns = [
    path(route = '', view = getData, name= "ApiHomePage"),
    path(route='Class/', view = sendAllClass, name="Get All Data From Class" ),
    path(route='Class/<int:id>', view=sendUniqueData, name="Get a One Data"),
]