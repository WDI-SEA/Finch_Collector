from django.db import models

# Create your models here.
class Duck(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color,
        }