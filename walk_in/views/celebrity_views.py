from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers import CelebritySerializer
from ..models import Celebrity

class Celebrities(APIView):
    def get(self, request):
        """Index Request"""
        print(request.session)
        celebrities = Celebrity.objects.all()[:10]
        data = CelebritySerializer(celebrities, many=True).data
        return Response(data)

    def post(self, request):
        """Post request"""
        print(request.data)
        celebrity = CelebritySerializer(data=request.data)
        if celebrity.is_valid():
            celebrity.save()
            return Response(celebrity.data, status=status.HTTP_201_CREATED)
        else:
            return Response(celebrity.errors, status=status.HTTP_400_BAD_REQUEST)

class CelebrityDetail(APIView):
    def get(self, request, pk):
        """Show request"""
        celebrity = get_object_or_404(Celebrity, pk=pk)
        data = CelebritySerializer(celebrity).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        celebrity = get_object_or_404(Celebrity, pk=pk)
        ms = CelebritySerializer(celebrity, data=request.data)
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        celebrity = get_object_or_404(Celebrity, pk=pk)
        celebrity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)