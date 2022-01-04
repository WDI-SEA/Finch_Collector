from django.urls import path
from django.urls import path
from .views import SuperHeroDetailView, SuperheroesView

urlpatterns = [
    path('', SuperheroesView.as_view(), name='heroes'),
    path('<int:pk>/', SuperHeroDetailView.as_view(), name='Hero-detail')
]