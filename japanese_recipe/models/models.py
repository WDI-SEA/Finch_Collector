from django.db import models

# Create your models here.
class Recipe(models.Model):
    """Defining my recipe model"""
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    url = models.CharField(max_length=200, default="")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """returns a string representation of the model"""
        return self.title

    def as_dict(self):
        """This returns a dict of the Book Instance"""
        return {
                'id': self.id,
                'title': self.title,
                'author': self.author,
                'content': self.content,
                'url': self.url
                }
