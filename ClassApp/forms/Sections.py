from django import forms as fm;
from ..models.Section import Class_Section as model;

class Class_Section_Form(fm.ModelForm):
    class Meta:
        model = model;
        fields = [
            'Name',
            'Info',
            'Class',
        ]
        