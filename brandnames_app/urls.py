# first_app/urls.py
from django.urls import path
from .views.brand_views import BrandsView, BrandDetailView
from .views.store_views import Stores, StoreDetail
from .views.location_views import Locations, LocationDetail

urlpatterns = [
    path('', BrandsView.as_view(), name='brands'),
    path('<int:pk>/', BrandDetailView.as_view(), name='brand-detail'),
    path('stores', Stores.as_view(), name='stores'),
    path('stores/<int:pk>', StoreDetail.as_view(), name='store_detail'),
    path('locations', Locations.as_view(), name='locatioins'),
    path('locations/<int:pk>', LocationDetail.as_view(), name='location_detail'),
]