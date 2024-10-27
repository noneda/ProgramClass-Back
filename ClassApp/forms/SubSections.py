from django import forms as fm;
from ..models.SubSection import Class_SubSection as model;

class Class_SubSection_Form(fm.ModelForm):
    class Meta:
        model = model;
        fields = [
            'Name',
            'Info',
            'Video',
            'Section'
        ]
        