from django.db import models

# Create your models here.
class Bag(models.Model):
    """Define fields and methods for bags"""
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Print bag brand and name"""
        return self.brand + self.name
    
    # as_dict needed before serializer integrated with 'show' route
    def as_dict(self):
        """return bag as dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'brand': self.brand
        }

class Celebrity(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Print name"""
        return self.first_name + self.last_name

class ProductPlacement(models.Model):
    celebrity = models.ForeignKey('Celebrity', on_delete=models.CASCADE)
    bag = models.ForeignKey('Bag', on_delete=models.CASCADE)

    photograhed = models.DateField(auto_now=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)