from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .owner import Owner
from .serializers import OwnerSerializer

# Create your views here.
class Owner(APIView):
    def get(self, request):
        """Index Request"""
        print(request.session)
        owner = Owner.objects.all()[:10]
        data = OwnerSerializer(owner, many=True).data
        return Response(data)

    serializer_class = OwnerSerializer
    def post(self, request):
        """Post request"""
        print(request.data)
        owner = OwnerSerializer(data=request.data)
        if owner.is_valid():
            b = owner.save()
            return Response(owner.data, status=status.HTTP_201_CREATED)
        else:
            return Response(owner.errors, status=status.HTTP_400_BAD_REQUEST)

class OwnerDetail(APIView):
    def get(self, request, pk):
        """Show request"""
        owner = get_object_or_404(Owner, pk=pk)
        data = OwnerSerializer(owner).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        owner = get_object_or_404(Owner, pk=pk)
        ms = OwnerSerializer(owner, data=request.data)
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        owner = get_object_or_404(Owner, pk=pk)
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
