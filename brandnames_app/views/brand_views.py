# first_app/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404


from ..models.brand import Brand
from ..serializers import BrandSerializer

# Create your views here.

class BrandsView(APIView):
    """Class for Index and Post"""

    def get(self, request):
        """Index Brands"""
        brands = Brand.objects.all()
        data = BrandSerializer(brands, many=True).data
        return Response(data)

    def post(self, request):
        """Create Brands"""
        print(request.data)
        brand = BrandSerializer(data=request.data)
        if brand.is_valid():
            brand.save()
            return Response(brand.data, status=status.HTTP_201_CREATED)
        else:
            return Response(brand.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandDetailView(APIView):
    def get(self, request, pk):
        """Show one brand"""
        brand = get_object_or_404(Brand, pk=pk)
        data = BrandSerializer(brand).data
        return Response(data)

    def delete(self, request, pk):
        """Deletes a brand"""
        brand = get_object_or_404(Brand, pk=pk)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        """Update a brand"""
        # first we locate the brand
        brand = get_object_or_404(Brand, pk=pk)
        # then we run our update through the serializer
        updated_brand = BrandSerializer(brand, data=request.data)
        if updated_brand.is_valid():
            updated_brand.save()
            return Response(updated_brand.data)
        return Response(updated_brand.errors, status=status.HTTP_400_BAD_REQUEST)
