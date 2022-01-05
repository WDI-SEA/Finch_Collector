# first_app/urls.py
from django.urls import path
from .views import BrandsView, BrandDetailView

urlpatterns = [
    path('', BrandsView.as_view(), name='Brands'),
    path('<int:pk>/', BrandDetailView.as_view(), name='Brand-detail')
]