from django.db import models;


class Class(models.Model):
    title = models.CharField(max_length=200);
    text = models.TextField(max_length=500);
    