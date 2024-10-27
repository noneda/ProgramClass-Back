from django import forms as fm;
from ..models.Question import Class_Question as model;

class Class_Question_Form(fm.ModelForm):
    class Meta:
        model = model;
        fields = [
            'Info',
            'Question',
            'Answer',
            'Section'
        ]
        