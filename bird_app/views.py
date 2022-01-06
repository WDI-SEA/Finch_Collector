from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AviarySerializer, BirdSerializer

from .models import Aviary, Bird

class BirdsView(APIView):
    def get(self, request):
        birds = Bird.objects.all()
        data = BirdSerializer(birds, many=True).data
        return Response(data)

    def post(self, request):
        print(request.data)
        bird = BirdSerializer(data=request.data)
        if bird.is_valid():
            bird.save()
            return Response(bird.data, status=status.HTTP_201_CREATED)
        else:
            return Response(bird.errors, status=status.HTTP_400_BAD_REQUEST)

class BirdDetailView(APIView):
    def get(self, request, pk):
        # show one bird
        bird = get_object_or_404(Bird, pk=pk)
        data = BirdSerializer(bird).data
        return Response(data)
    def delete(self, request, pk):
        # delete one bird
        bird = get_object_or_404(Bird, pk=pk)
        bird.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def patch(self, request, pk):
        # patch (update) a bird
        bird = get_object_or_404(Bird, pk=pk)
        updated_bird = BirdSerializer(bird, data=request.data)
        if updated_bird.is_valid():
            updated_bird.save()
            return Response(updated_bird.data)
        else:
            return Response(updated_bird.errors, status=status.HTTP_400_BAD_REQUEST)

class AviaryView(APIView):
    def get(self, request):
        aviaries = Aviary.objects.all()
        data = AviarySerializer(aviaries, many=True).data
        return Response(data)