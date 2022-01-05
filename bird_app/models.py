from django.db import models

class Bird(models.Model):
    name = models.CharField(max_length=50)
    sci_name = models.CharField(max_length=50)
    avg_wingspan = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)