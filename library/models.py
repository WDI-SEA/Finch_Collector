from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class KDrama(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    plot = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'genre': self.genre,
            'plot': self.plot
        }