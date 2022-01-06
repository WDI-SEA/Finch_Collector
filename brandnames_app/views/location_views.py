from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.location import Location
from ..serializers import LocationSerializer

# Create your views here.
class Locations(APIView):
    def get(self, request):
        """Index Request"""
        locations = Location.objects.all()[:10]
        data = LocationSerializer(locations, many=True).data
        return Response(data)

    serializer_class = LocationSerializer
    def post(self, request):
        """Post request"""
        print(request.data)
        location = LocationSerializer(data=request.data)
        if location.is_valid():
            b = location.save()
            return Response(location.data, status=status.HTTP_201_CREATED)
        else:
            return Response(location.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationDetail(APIView):
    def get(self, request, pk):
        """Show request"""
        location = get_object_or_404(Location, pk=pk)
        print(location.stores.all())
        data = LocationSerializer(location).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        location = get_object_or_404(Location, pk=pk)
        ms = LocationSerializer(location, data=request.data)
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        location = get_object_or_404(Location, pk=pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)