from django.urls import path
from .views import HeroView, HeroDetailView

urlpatterns = [
    path('', HeroView.as_view(), name='Heroes'),
    path('<int:pk>/', HeroDetailView.as_view(), name='hero-detail')
]