from rest_framework import serializers

from .models import Bag, Celebrity, ProductPlacement

# create class for Bag serializer
class BagSerializer(serializers.ModelSerializer):
    # define meta class
    class Meta:
        # specify model whose fields we want to use
        model = Bag
        # specify fields
        fields = '__all__'


class CelebritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity
        fields = '__all__'

class ProductPlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPlacement
        fields = '__all__'

class ProductPlacementReadSerializer(serializers.ModelSerializer):
    celebrity = serializers.StringRelatedField()
    bag = serializers.StringRelatedField()
    class Meta:
        model = ProductPlacement
        fields = '__all__'

