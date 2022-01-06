# import serializers from the django rest framework
from rest_framework import serializers

# import our model
from .models import Cats
from .owner import Owner

# create our serializer class
# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
class CatsSerializer(serializers.ModelSerializer):
    # define meta class
    class Meta:
        # specify the model from which to define the fields
        model = Cats
        # define the fields to be returned
        fields = '__all__'
        
class CatsReadSerializer(serializers.ModelSerializer):
  owner = serializers.StringRelatedField()
  class Meta:
    model = Cats
    fields = '__all__'
    
        
class OwnerSerializer(serializers.ModelSerializer):
  owner_cat = CatsSerializer(many=True, read_only=True)
  class Meta:
    model = Owner
    fields = '__all__'