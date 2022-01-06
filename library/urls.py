from django.urls import path
from .views.dogs_views import DogsView, DogsDetailView
from .views.toy_views import ToysView, ToyDetail

urlpatterns = [
    path('', DogsView.as_view(), name='Dogs'),
    path('<int:pk>/', DogsDetailView.as_view(), name='Dog-Detail'),
    path('toys', ToysView.as_view(), name='toys'),
    path('toys/<int:pk>', ToyDetail.as_view(), name='toy_detail'),
]




