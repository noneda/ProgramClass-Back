from django.db import models;
from .Section import Class_Section;

class  Class_Question(models.Model):
    Info = models.CharField(max_length=200);
    Question = models.CharField(max_length=400);
    Answer = models.TextField(max_length=500);
    Section = models.ForeignKey(Class_Section, on_delete=models.CASCADE);