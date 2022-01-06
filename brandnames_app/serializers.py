# import serializers from the django rest framework
from rest_framework import serializers

# import our model
from .models.brand import Brand
from .models.location import Location
from .models.store import Store

# create our serializer class
# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer


class BrandSerializer(serializers.ModelSerializer):
    # define meta class
    class Meta:
        # specify the model from which to define the fields
        model = Brand
        # define the fields to be returned
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    located_brands = serializers.StringRelatedField(many=True)

    class Meta:
        model = Location
        fields = '__all__'


class StoreReadSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    location = LocationSerializer()

    class Meta:
        model = Store
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
