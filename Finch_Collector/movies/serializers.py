# Import serializers from django rest framework
from rest_framework import serializers

# Import our model
from .models import Movies

# Create our serializer class
# django-rest-framework.org/api-quide/serializers/#modelserializer
class MovieSerializer(serializers.ModelSerializer):
    # define meta class
    class Meta:
        #specify the model from which to define the fields
        model = Movies
        #define fields to be returned
        fields = '__all__'
