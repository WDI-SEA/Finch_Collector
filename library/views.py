from django.shortcuts import get_object_or_404, render
# from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CatsSerializer
from .models import Cats

# Create your views here.
class CatsView(APIView):
    """Class for Index and Post"""
    def get(self, request):
        """Index Books"""
        cats = Cats.objects.all()
        data = CatsSerializer(cats, many=True).data
        return Response(data)
    
    def post(self, request):
        """Create Cats"""
        print(request.data)
        cats = CatsSerializer(data=request.data)
        if cats.is_valid():
            cats.save()
            return Response(cats.data, status=status.HTTP_201_CREATED)
        else:
            return Response(cats.errors, status=status.HTTP_400_BAD_REQUEST)

# def index(request):
#     books = Book.objects.all()
#     data = { 'books': list(books.values()) }
#     return JsonResponse(data)

# def show(request, pk):
#     # https://docs.djangoproject.com/en/3.0/ref/models/querysets/#get
#     book = Book.objects.get(pk=pk).as_dict()
#     return JsonResponse(book)

class CatsDetailView(APIView):
    def get(self, request, pk):
        cats = get_object_or_404(Cats, pk=pk)
        data = CatsSerializer(cats).data
        return Response(data)
    
    def delete(self, request, pk):
        cats = get_object_or_404(Cats, pk=pk)
        cats.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        cats = get_object_or_404(Cats, pk=pk)
        # then we run our update through the serializer
        updated_cats = CatsSerializer(cats, data=request.data)
        if updated_cats.is_valid():
            updated_cats.save()
            return Response(updated_cats.data)
        return Response(updated_cats.errors, status=status.HTTP_400_BAD_REQUEST)