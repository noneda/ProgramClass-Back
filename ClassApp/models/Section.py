from django.db import models;
from .Class  import Class


class Section(models.Model):
    Name = models.CharField(max_length=100)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)