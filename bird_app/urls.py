from django.urls import path
from .views import AviaryView, BirdsView, BirdDetailView

urlpatterns = [
    path('birds/', BirdsView.as_view(), name='Birds'),
    path('<int:pk>/', BirdDetailView.as_view(), name='Bird-detail'),
    path('aviaries/', AviaryView.as_view(), name='Aviaries')
]