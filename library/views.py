from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from.serializers import PlayerSerializer
from .models import Player

# Create your views here.
class PlayersView(APIView):
    def get(self, request):
        players = Player.objects.all()
        data = PlayerSerializer(players, many = True).data
        return Response(data)
    
    def post(self, request):
        print(request.data)
        player = PlayerSerializer(data = request.data)
        if player.is_valid():
            player.save()
            return Response(player.data, status=status.HTTP_201_CREATED)
        else:
            return Response(player.errors, status = status.HTTP_400_BAD_REQUEST)

class PlayersDetailView(APIView):
    def get(self, request, pk):
        player = get_object_or_404(Player, pk=pk)
        data = PlayerSerializer(player).data
        return Response(data)

    def delete(self, request, pk):
        player = get_object_or_404(Player, pk=pk)
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        player = get_object_or_404(Player, pk=pk)
        updated_player = PlayerSerializer(player, data=request.data)
        if updated_player.is_valid():
            updated_player.save()
            return Response(updated_player.data)
        return Response(updated_player.errors, status=status.HTTP_400_BAD_REQUEST)