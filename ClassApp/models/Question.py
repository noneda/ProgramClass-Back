from django.db import models;
from .Section import Class_Section;

class  Class_Question(models.Model):
    Name = models.CharField(max_length=200);
    Section = models.ForeignKey(Class_Section, on_delete=models.CASCADE);
    Order = models.IntegerField(default=0)
