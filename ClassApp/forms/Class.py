from django import forms as fm;
from ..models.Class import Class_Main as model;

class Class_Main_Form(fm.ModelForm):    
    class Meta:
        model = model;
        fields = '__all__'
        