from django.db import models
from .dog import Dog


class Toy(models.Model):
    toy_name = models.CharField(max_length=100)

    dog = models.ForeignKey(
        Dog,
        on_delete=models.CASCADE,
        related_name='owned_toys'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.toy_name}"