from django.db import models

# Create your models here.
class TradingCard(models.Model):
    """Defines fields and methods of the TradingCard resource model"""
    # define our fields here
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/
    player = models.CharField(max_length=100)
    league = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # https://docs.djangoproject.com/en/3.0/ref/models/instances/#str
    # here we'll set up our __str__ method and our as_dict method
    def __str__(self):
        """Returns a string depiction of the model"""
        return self.title
    
    # This will be used before we have a serializer in the 'show' method request
    def as_dict(self):
        """returns dictionary version of the TradingCard instance"""
        return {
            'id': self.id,
            'player': self.player,
            'league': self.league,
            'year': self.year,
            'brand': self.brand,
        }