from django.urls import path
from .views import RecipeView, RecipeDetailView

urlpatterns = [
    path('', RecipeView.as_view(), name='Recipe'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='Recipe-Detail')    
    ]
