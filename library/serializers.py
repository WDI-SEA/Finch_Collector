from rest_framework import serializers

from .models.dog import Dog
from .models.toy import Toy


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = '__all__'

class ToyReadSerializer(serializers.ModelSerializer):
    dog = serializers.StringRelatedField()
    class Meta:
        model = Toy
        fields = '__all__'

class DogSerializer(serializers.ModelSerializer):
    owned_toys = ToySerializer(many=True, read_only=True)
    class Meta:
        model = Dog
        fields = '__all__'