# import serializers from the django rest framework
from rest_framework import serializers

# import our model
from .models import Anime

# create our serializer class
# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
class AnimeSerializer(serializers.ModelSerializer):
    # define meta class
    class Meta:
        # specify the model from which to define the fields
        model = Anime
        # define the fields to be returned
        fields = '__all__'
        # fields = ['title', 'author']