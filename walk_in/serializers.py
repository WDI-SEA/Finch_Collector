from rest_framework import serializers

from .models import Bag

# create class for Bag serializer
class BagSerializer(serializers.ModelSerializer):
    # define meta class
    class Meta:
        # specify model whose fields we want to use
        model = Bag
        # specify fields
        fields = '__all__'