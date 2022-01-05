from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SightingSerializer
from .models import Sighting

# Create your views here.

# def index(request):
#   return HttpResponse('<h1>Welcome to our campus! FUN! /ᐠ｡‸｡ᐟ\ﾉ</h1>')

class SightingsView(APIView):
    """Class for Index and Post"""
    def get(self, request):
        """Index Books"""
        books = Sighting.objects.all()
        data = SightingSerializer(books, many=True).data
        return Response(data)
    
    def post(self, request):
        """Create Sightings"""
        print(request.data)
        sighting = SightingSerializer(data=request.data)
        if sighting.is_valid():
            sighting.save()
            return Response(sighting.data, status=status.HTTP_201_CREATED)
        else:
            return Response(sighting.errors, status=status.HTTP_400_BAD_REQUEST)

class SightingDetailView(APIView):
    def get(self, request, pk):
        """Show one book"""
        sighting = get_object_or_404(Sighting, pk=pk)
        data = SightingSerializer(sighting).data
        return Response(data)

    def delete(self, request, pk):
        """Deletes a book"""
        sighting = get_object_or_404(Sighting, pk=pk)
        sighting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        """update a book"""
        # first locate the book
        sighting = get_object_or_404(Sighting, pk=pk)
        # run update through serializer
        updated_sighting = SightingSerializer(sighting, data=request.data)
        if updated_sighting.is_valid():
            updated_sighting.save()
            return Response(updated_sighting.data)
        return Response(updated_sighting.errors, status=status.HTTP_400_BAD_REQUEST)