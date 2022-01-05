from django.shortcuts import get_object_or_404, render
from .serializers import MovieSerializer
from .models import Movies
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class MoviesView(APIView):
    def get(self, request):
        movies = Movies.objects.all()
        data = MovieSerializer(movies, many=True).data
        return Response(data)

    def post(self, request):
        """Create Movies"""
        print(request.data)
        movie = MovieSerializer(data=request.data)
        if movie.is_valid():
            movie.save()
            return Response(movie.data, status=status.HTTP_201_CREATED)
        else:
            return Response(movie.errors, status=status.HTTP_404_BAD_REQUEST)

class MovieDetailView(APIView):
    def get(self, request, pk):
        """Show one movie"""
        movie = get_object_or_404(Movies, pk=pk)
        data = MovieSerializer(movie).data
        return Response(data)

    def delete(self, request, pk):
        """Delete's a movie"""
        movie = get_object_or_404(Movies, pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        movie = get_object_or_404(Movies, pk=pk)
        updated_movie = MovieSerializer(movie, data=request.data)
        if updated_movie.is_valid():
            updated_movie.save()
            return Response(updated_movie.data)
        else:
            return Response(updated_movie.errors, status=status.HTTP_400_BAD_REQUEST)