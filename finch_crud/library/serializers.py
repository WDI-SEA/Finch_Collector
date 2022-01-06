# import serializers from the django rest framework
from rest_framework import serializers


# import our model
from .models.car import Car
from .models.owner import Owner

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class CarReadSerializer(serializers.ModelSerializer):
    car_owner = serializers.StringRelatedField()
    class Meta:
        model = Car
        fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    owned_cars = CarSerializer(many=True, read_only=True)
    class Meta:
        model = Owner
        fields = '__all__'