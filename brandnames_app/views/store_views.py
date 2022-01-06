from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.store import Store
from ..serializers import StoreSerializer, StoreReadSerializer

# Create your views here.
class Stores(APIView):
    def get(self, request):
        """Index Request"""
        stores = Store.objects.all()[:10]
        data = StoreReadSerializer(stores, many=True).data
        return Response(data)

    serializer_class = StoreSerializer
    def post(self, request):
        """Post request"""
        print(request.data)
        store = StoreSerializer(data=request.data)
        if store.is_valid():
            b = store.save()
            return Response(store.data, status=status.HTTP_201_CREATED)
        else:
            return Response(store.errors, status=status.HTTP_400_BAD_REQUEST)

class StoreDetail(APIView):
    def get(self, request, pk):
        """Show request"""
        store = get_object_or_404(Store, pk=pk)
        data = StoreReadSerializer(store).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        store = get_object_or_404(Store, pk=pk)
        ms = StoreSerializer(store, data=request.data)
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        store = get_object_or_404(Store, pk=pk)
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)