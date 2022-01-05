# import serializers from the django rest framework
from rest_framework import serializers

# import our model
from .models import TradingCard

# create our serializer class
# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
class TradingCardSerializer(serializers.ModelSerializer):
    # define meta class
    class Meta:
        # specify the model from which to define the fields
        model = TradingCard
        # define the fields to be returned
        fields = '__all__'