from rest_framework import serializers

from .models import KDrama

class KDramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = KDrama
        fields = '__all__'