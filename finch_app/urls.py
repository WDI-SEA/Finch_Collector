from django.urls import path
from .views import DogDetailView, DogsView

urlpatterns = [
    path('', DogsView.as_view(), name='Dogs'),
    path('<int:pk>/', DogDetailView.as_view(), name='Dog-detail')
]
