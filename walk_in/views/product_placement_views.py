from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers import ProductPlacementSerializer, ProductPlacementReadSerializer
from ..models import ProductPlacement

class ProductPlacements(APIView):
    def get(self, request):
        """Index Request"""
        print(request.session)
        pps = ProductPlacement.objects.all()[:10]
        data = ProductPlacementReadSerializer(pps, many=True).data
        return Response(data)

    def post(self, request):
        """Post request"""
        print(request.data)
        pp = ProductPlacementSerializer(data=request.data)
        if pp.is_valid():
            pp.save()
            return Response(pp.data, status=status.HTTP_201_CREATED)
        else:
            return Response(pp.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductPlacementDetail(APIView):
    def get(self, request, pk):
        """Show request"""
        pp = get_object_or_404(ProductPlacement, pk=pk)
        data = ProductPlacementReadSerializer(pp).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        pp = get_object_or_404(ProductPlacement, pk=pk)
        ms = ProductPlacementSerializer(pp, data=request.data)
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        pp = get_object_or_404(ProductPlacement, pk=pk)
        pp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)