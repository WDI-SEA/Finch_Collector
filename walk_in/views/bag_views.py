from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers import BagSerializer
from ..models import Bag

# Create your views here.

class BagsView(APIView):
    """Index view and Post route"""
    def get(self, request):
        """Bags Index"""
        bags = Bag.objects.all()
        data = BagSerializer(bags, many=True).data
        return Response(data)
    
    def post(self, request):
        """Create Bags"""
        print(request.data)
        bag = BagSerializer(data=request.data)
        if bag.is_valid():
            bag.save()
            return Response(bag.data, status=status.HTTP_201_CREATED)
        else:
            return Response(bag.errors, status=status.HTTP_400_BAD_REQUEST)

class BagDetailView(APIView):
    def get(self, request, pk):
        """Show One Bag"""
        bag = get_object_or_404(Bag, pk=pk)
        data = BagSerializer(bag).data
        return Response(data)
    
    def delete(self, request, pk):
        """Delete a bag"""
        bag = get_object_or_404(Bag, pk=pk)
        bag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        """Update a Bag"""
        # secure the bag
        bag = get_object_or_404(Bag, pk=pk)
        #then serialize the update req
        updated_bag = BagSerializer(bag, data=request.data)
        if updated_bag.is_valid():
            updated_bag.save()
            return Response(updated_bag.data)
        return Response(updated_bag.errors, status=status.HTTP_400_BAD_REQUEST)
