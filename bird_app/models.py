from django.db import models

class Bird(models.Model):
    name = models.CharField(max_length=50)
    sci_name = models.CharField(max_length=50)
    avg_wingspan = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Aviary(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length= 30)
    state = models.CharField(max_length=2)
    birds = models.ManyToManyField('Bird')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
