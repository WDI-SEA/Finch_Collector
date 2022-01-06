from django.db import models
from .owner import Owner


class Cats(models.Model):

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        related_name='cat_owner'
    )
    # updated_at = models.DateTimeField(auto_now=True)
    # created_at = models.DateTimeField(auto_now_add=True)

   
    def __str__(self):
        
        return self.name
