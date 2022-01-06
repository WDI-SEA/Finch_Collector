from django.db import models
from .brand import Brand
from .store import Store

class Location(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    located_brands = models.ManyToManyField(
        # locations can have many brands and brands can be in many locations
        Brand,
        through=Store,
        through_fields=('location', 'brand')
    )
    def __str__(self):
        return f"{self.city} {self.country}"