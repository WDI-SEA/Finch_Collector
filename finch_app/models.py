from django.db import models

# Create your models here.
class Sighting(models.Model):
    """Defines fields and methods of the Book resource model"""
    # define our fields here
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # https://docs.djangoproject.com/en/3.0/ref/models/instances/#str
    # here we'll set up our __str__ method and our as_dict method
    def __str__(self):
        """Returns a string depiction of the model"""
        return self.type
    
    # This will be used before we have a serializer in the 'show' method request
    def as_dict(self):
        """returns dictionary version of the Sighting instance"""
        return {
            'id': self.id,
            'type': self.type,
            'description': self.description,
            'location': self.location
        }