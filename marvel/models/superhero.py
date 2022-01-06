from django.db import models

from .team import Team

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=100)
    movie = models.CharField(max_length=100)
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='team_ons'
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'movie': self.movie
        }