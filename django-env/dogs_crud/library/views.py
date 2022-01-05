from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
# django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import DogSerializer
from .models import Dog

# Create your views here.
class DogsView(APIView):
    """Class for Index and Post"""
    def get(self, request):
        """Index Dogs"""
        dogs = Dog.objects.all()
        data = DogSerializer(dogs, many=True).data
        return Response(data)

    def post(self, request):
        """Create Dogs"""
        print(request.data)
        dog = DogSerializer(data=request.data)
        if dog.is_valid():
            dog.save()
            return Response(dog.data, status=status.HTTP_201_CREATED)
        else:
            return Response(dog.errors, status=status.HTTP_400_BAD_REQUEST)

# def index(request):
#     dogs = Dog.objects.all()
#     data = { 'dogs': list(dogs.values()) }
#     return JsonResponse(data)

# def show(request, pk): 
#     # https://docs.djangoproject.com/en/3.0/ref/models/querysets/#get
#     dog = Dog.objects.get(pk=pk).as_dict()
#     return JsonResponse(dog)

class DogDetailView(APIView): 
    def get(self, request, pk): 
        """Show one dog"""
        dog = get_object_or_404(Dog, pk=pk)
        data = DogSerializer(dog).data
        return Response(data)

    def delete(self, request, pk):
        """Deletes a dog"""
        dog = get_object_or_404(Dog, pk=pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        """Update a Dog"""
        # first we locate the dog
        dog = get_object_or_404(Dog, pk=pk)
        # then we run our update through the serializer
        updated_dog = DogSerializer(dog, data=request.data)
        if updated_dog.is_valid():
            updated_dog.save()
            return Response(updated_dog.data)
        return Response(updated_dog.errors, status=status.HTTP_400_BAD_REQUEST)