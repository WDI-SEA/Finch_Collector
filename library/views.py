from django.shortcuts import get_object_or_404, render
# from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AnimeSerializer
from .models import Anime

# Create your views here.
class AnimeView(APIView):
    """Class for Index and Post"""
    def get(self, request):
        """Index Books"""
        anime = Anime.objects.all()
        data = AnimeSerializer(anime, many=True).data
        return Response(data)
    
    def post(self, request):
        """Create Books"""
        print(request.data)
        anime = AnimeSerializer(data=request.data)
        if anime.is_valid():
            anime.save()
            return Response(anime.data, status=status.HTTP_201_CREATED)
        else:
            return Response(anime.errors, status=status.HTTP_400_BAD_REQUEST)

# def index(request):
#     books = Book.objects.all()
#     data = { 'books': list(books.values()) }
#     return JsonResponse(data)

# def show(request, pk):
#     # https://docs.djangoproject.com/en/3.0/ref/models/querysets/#get
#     book = Book.objects.get(pk=pk).as_dict()
#     return JsonResponse(book)

class AnimeDetailView(APIView):
    def get(self, request, pk):
        """Show one anime"""
        anime = get_object_or_404(Anime, pk=pk)
        data = AnimeSerializer(anime).data
        return Response(data)
    
    def delete(self, request, pk):
        """Deletes an anime"""
        anime = get_object_or_404(Anime, pk=pk)
        anime.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        """Update a Anime"""
        # first we locate the anime
        anime = get_object_or_404(Anime, pk=pk)
        # then we run our update through the serializer
        updated_anime = AnimeSerializer(anime, data=request.data)
        if updated_anime.is_valid():
            updated_anime.save()
            return Response(updated_anime.data)
        return Response(updated_anime.errors, status=status.HTTP_400_BAD_REQUEST)