from django.db import models;
from .Question import Class_Question;


class Class_SubQuestion(models.Model):
    Ask = models.CharField(max_length=400);
    Answer = models.TextField(max_length=500);
    Type = models.CharField(max_length=200);
    Question = models.ForeignKey(Class_Question, on_delete=models.CASCADE);
    Order = models.IntegerField(default=0);
    