from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers import HeroSerializer, HeroReadSerializer
from ..models.superhero import Hero

class Heroes(APIView):
    def get(self, request):
        superhero = Hero.objects.all()[:10]
        data = HeroReadSerializer(superhero, many=True).data
        return Response(data)

    def post(self, request):
        print(request.data)
        superhero = HeroSerializer(data=request.data)
        if superhero.is_valid():
            superhero.save()
            return Response(superhero.data, status=status.HTTP_201_CREATED)
        else:
            return Response(superhero.errors, status=status.HTTP_400_BAD_REQUEST)
    
class HeroDetail(APIView):
    def get(self, request, pk):
        superhero = get_object_or_404(Hero, pk=pk)
        data = HeroReadSerializer(superhero).data
        return Response(data)

    def delete(self, request, pk):
        superhero = get_object_or_404(Hero, pk=pk)
        superhero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        superhero = get_object_or_404(Hero, pk=pk)
        updated_hero = HeroSerializer(superhero, data=request.data)
        if updated_hero.is_valid():
            updated_hero.save()
            return Response(updated_hero.data)
        return Response(updated_hero.errors, status=status.HTTP_400_BAD_REQUEST)

