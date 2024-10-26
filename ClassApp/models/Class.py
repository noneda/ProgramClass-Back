from django.db import models;

class Class_Main(models.Model):
    title = models.CharField(max_length=200);
    text = models.TextField(max_length=500);
    type = models.CharField(max_length=200);