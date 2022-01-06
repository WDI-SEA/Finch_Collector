from rest_framework import serializers

from .models.superhero import Hero
from .models.team import Team

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'

class HeroReadSerializer(serializers.ModelSerializer):
    team = serializers.StringRelatedField()
    class Meta:
        model = Hero
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    team_ons = HeroSerializer(many=True, read_only=True)
    class Meta:
       model = Team
       fields = '__all__'
