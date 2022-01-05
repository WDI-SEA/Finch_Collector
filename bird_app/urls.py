from django.urls import path
from .views import BirdsView, BirdDetailView

urlpatterns = [
    path('', BirdsView.as_view(), name='Birds'),
    path('<int:pk>/', BirdDetailView.as_view(), name='Bird-detail')
]