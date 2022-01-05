# import serializers from the django rest framework
from rest_framework import serializers

# import our model
from .models import Car

# create our serializer class

class CarSerializer(serializers.ModelSerializer):
    # define meta class
    class Meta:
        # specify the model from which to define the fields
        model = Car
        # define the fields to be returned
        fields = '__all__'