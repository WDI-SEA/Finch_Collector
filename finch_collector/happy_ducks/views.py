from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import DuckSerializer
from .models import Duck

# Create your views here.
class DuckView(APIView):
    def get(self, request):
        duck = Duck.objects.all()
        data = DuckSerializer(duck, many=True).data
        return Response(data)
    def post(self, request):
        print(request.data)
        duck = DuckSerializer(data=request.data)
        if duck.is_valid():
            duck.save()
            return Response(duck.data, status=status.HTTP_201_CREATED)
        else:
            return Response(duck.errors, status=status.HTTP_400_BAD_REQUEST)

class DuckDetailView(APIView):
    def get(self, request, pk):
        duck = get_object_or_404(Duck, pk=pk)
        data = DuckSerializer(duck).data
        return Response(data)
    
    def delete(self, request, pk):
        duck = get_object_or_404(Duck, pk=pk)
        duck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def path(self, request, pk):
        update_duck = DuckSerializer(Duck, data=request.data)
        if update_duck.is_valid():
            update_duck.save()
            return Response(update_duck.data)
        return Response(update_duck.errors, status=status.HTTP_400_BAD_REQUEST)