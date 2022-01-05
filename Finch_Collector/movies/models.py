from django.db import models

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=150)
    director = models.CharField(max_length=50)
    release_date = models.IntegerField()