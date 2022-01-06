from django.db import models
from .owner import Owner

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(default=2022)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    car_owner = models.ForeignKey(
        Owner,
        related_name='owned_cars',
        on_delete=models.CASCADE
        
  )
    def __str__(self):
        return f"{self.make}"
    
   
   
