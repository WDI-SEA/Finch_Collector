from django.urls import path
from .views.car_views import CarView, CarDetailView
from .views.owner_views import Owners

urlpatterns = [
    path('', CarView.as_view(), name='Cars'),
    path('<int:pk>/', CarDetailView.as_view(), name= 'Car-detail'),
    path('owner', Owners.as_view(), name = 'owners')
    ]