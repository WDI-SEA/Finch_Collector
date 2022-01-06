from rest_framework import serializers

from .models import Aviary, Bird

class BirdSerializer(serializers.ModelSerializer):
    aviaries = serializers.StringRelatedField()
    class Meta:
        model = Bird
        fields = '__all__'

class AviarySerializer(serializers.ModelSerializer):
    birds = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Aviary
        fields = '__all__'