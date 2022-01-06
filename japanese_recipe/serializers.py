from rest_framework import serializers
# model import
from .models import Recipe, User

# Initializing Serializer Class
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = '__all__'
