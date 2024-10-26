from django.db import models;
from .Class  import Class_Main

class Class_Section(models.Model):
    Name = models.CharField(max_length=100)
    Info = models.TextField();
    Class = models.ForeignKey(Class_Main, on_delete=models.CASCADE)
