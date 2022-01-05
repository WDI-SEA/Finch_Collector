from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RecipeSerializer
# Model Imports
from .models import Recipe
# Create your views here.

class RecipeView(APIView):
    """Class for Index and Post"""
    def get(self, request):
        """Recipe Index"""
        recipes = Recipe.objects.all()
        data = RecipeSerializer(recipes, many=True).data
        return Response(data)
        
    def post(self, request):
        """Create Recipe"""
        print(request.data)
        recipe = RecipeSerializer(data=request.data)
        if recipe.is_valid():
            recipe.save()
            return Response(recipe.data, status=status.HTTP_201_CREATED)
        else:
            return Response(recipe.errors, status=status.HTTP_400_BAD_REQUEST)

# def index(request):
#     books = Book.objects.all()
#     data = { 'books': list(books.values()) }
#     return JsonResponse(data)

# def show(request, pk):
#     # https://docs.djangoproject.com/en/3.0/ref/models/querysets/#get
#     book = Book.objects.get(pk=pk).as_dict()
#     return JsonResponse(book)

class RecipeDetailView(APIView):
    def get(self, request, pk):
        """Show one recipe"""
        recipe = get_object_or_404(Recipe, pk=pk)
        data = RecipeSerializer(recipe).data
        return Response(data)
    
    def delete(self, request, pk):
        """Deletes a Recipe"""
        recipe = get_object_or_404(Recipe, pk=pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        """Update a Recipe"""
        # first we locate the book
        recipe = get_object_or_404(Recipe, pk=pk)
        # then we run our update through the serializer
        updated_recipe = RecipeSerializer(recipe, data=request.data)
        if updated_recipe.is_valid():
            updated_recipe.save()
            return Response(updated_recipe.data)
        return Response(updated_recipe.errors, status=status.HTTP_400_BAD_REQUEST)

