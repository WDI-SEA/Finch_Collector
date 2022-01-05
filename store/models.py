from django.db import models

# Create your models here.
class Sneaker(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brand

    def as_dict(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'name': self.name,
            'color': self.color
        }

