from rest_framework import serializers
# model import
from .models import Recipe

# Initializing Serializer Class
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
