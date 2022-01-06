from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)
    
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)

    def __str__(self):
        return self.name