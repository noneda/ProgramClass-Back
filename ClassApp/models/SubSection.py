from django.db import models;
from .SubSection import SubSection

class SubSection(models.Model):
    Name = models.CharField(max_length=100)
    Section = models.ForeignKey(SubSection, on_delete=models.CASCADE)