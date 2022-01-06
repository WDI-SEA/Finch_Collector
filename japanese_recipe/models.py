from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Recipe(models.Model):
    """Defining my recipe model"""
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    url = models.CharField(max_length=200, default="")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    User = models.ForeignKey("User", on_delete=models.CASCADE)
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


class SavedRecipe(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='savedrecipe')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="savedrecipe")
    
    def __str__(self):
        return f"{self.recipe} {self.user}"


class User(models.Model):
    """defining my user model"""
    username = models.CharField(max_length=100)
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    fave_recipe = models.ManyToManyField(
    Recipe,
    through=SavedRecipe,
    through_fields=('recipe', 'user')
            )
    def __str__(self):
        return self.username

    def as_dict(self):
        return {
                'id': self.id,
                'username': self.username,
                }

