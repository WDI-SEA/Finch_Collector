from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SneakerSerializer
from .models import Sneaker

# Create your views here.
class SneakerView(APIView):
    def get(self, request):
        sneakers = Sneaker.objects.all()
        data = SneakerSerializer(sneakers, many=True).data
        return Response(data)

    def post(self, request):
        print(request.data)
        sneaker = SneakerSerializer(data=request.data)
        if sneaker.is_valid():
            sneaker.save()
            return Response(sneaker.data, status=status.HTTP_201_CREATED)
        else:
            return Response(sneaker.errors, status=status.HTTP_400_BAD_REQUEST)

class SneakerDetailView(APIView): 
    def get(self, request, pk):
        sneaker = get_object_or_404(Sneaker, pk=pk)
        data = SneakerSerializer(sneaker).data
        return Response(data)

    def delete(self, request, pk):
        sneaker = get_object_or_404(Sneaker, pk=pk)
        sneaker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk): 
        sneaker = get_object_or_404(Sneaker, pk=pk)
        updated_sneaker = SneakerSerializer(sneaker, data=request.data)
        if updated_sneaker.is_valid():
            updated_sneaker.save()
            return Response(updated_sneaker.data)
        return Response(updated_sneaker.errors, status=status.HTTP_400_BAD_REQUEST)   
