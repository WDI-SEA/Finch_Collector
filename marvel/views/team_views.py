from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.team import Team
from ..serializers import TeamSerializer 

class Teams(APIView):
    def get(self, request):
        team = Team.objects.all()[:10]
        data = TeamSerializer(team, many=True).data
        return Response(data)

    serializer_class = TeamSerializer
    def post(self, request):
        team = TeamSerializer(data=request.data)
        if team.is_valid():
            b = team.saved()
            return Response(team.data, status=status.HTTP_201_CREATED)
        else:
            return Response(team.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamDetail(APIView):
    def get(self, request, pk):
        team = get_object_or_404(Team, pk=pk)
        data = TeamSerializer(team).data
        return Response(data)

    def patch(self, request, pk):
        team = get_object_or_404(Team, pk=pk)
        ms = TeamSerializer(team, data=request.data)
        if ms.is_valid():
            b = ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        team = get_object_or_404(Team, pk=pk)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
