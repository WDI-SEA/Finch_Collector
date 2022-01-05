from django.db import models

# Create your models here.
class Dog(models.Model):
    breed = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.breed

    # This will be used before we have a serializer in the 'show' method request
    def as_dict(self):
        """returns dictionary version of the book instance"""
        return {
            'id': self.id,
            'breed': self.breed,
            'gender': self.gender
        }