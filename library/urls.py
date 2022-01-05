from django.urls import path
from .views import KDramaDetailView, KDramasView

urlpatterns = [
    path('', KDramasView.as_view(), name = 'KDramas'),
    path('<int:pk>/', KDramaDetailView.as_view(), name = 'KDrama-detail')
]