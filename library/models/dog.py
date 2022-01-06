from django.db import models

# Create your models here.
class Dog(models.Model):

    dog_name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dog_name}"

    # def as_dict(self):
    #     return {
    #         'id': self.id,
    #         'dog_name': self.dog_name,
    #         'breed': self.breed
    #     }