from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import KDramaSerializer
from .models import KDrama

# Create your views here.
class KDramasView(APIView):
    # index
    def get(self, request):
        kdramas = KDrama.objects.all()
        data = KDramaSerializer(kdramas, many = True).data
        return Response(data)
    
    # post
    def post(self, request):
        print(request.data)
        kdrama = KDramaSerializer(data = request.data)
        if kdrama.is_valid():
            kdrama.save()
            return Response(kdrama.data, status = status.HTTP_201_CREATED)
        else:
            return Response(kdrama.errors, status = status.HTTP_400_BAD_REQUEST)

class KDramaDetailView(APIView):
    # show
    def get(self, request, pk):
        kdrama = get_object_or_404(KDrama, pk = pk)
        data = KDramaSerializer(kdrama).data
        return Response(data)
    
    # delete
    def delete(self, request, pk):
        kdrama = get_object_or_404(KDrama, pk = pk)
        kdrama.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    # patch
    def patch(self, request, pk):
        kdrama = get_object_or_404(KDrama, pk = pk)
        updated_kdrama = KDramaSerializer(kdrama, data = request.data)
        if updated_kdrama.is_valid():
            updated_kdrama.save()
            return Response(updated_kdrama.data)
        return Response(updated_kdrama.errors, status = status.HTTP_400_BAD_REQUEST)