from django.db import models;
from .Section import Class_Section
class Class_SubSection(models.Model):
    Name = models.CharField(max_length=100)
    Info = models.TextField();
    Video = models.CharField(max_length=100)
    Section = models.ForeignKey(Class_Section, on_delete=models.CASCADE)
    Order = models.IntegerField(default=0)
