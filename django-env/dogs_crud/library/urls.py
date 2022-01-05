#library/urls.py
from django.urls import path
# from .views import index, show
from .views import DogsView, DogDetailView

urlpatterns = [
    # this was our path before using rest framework and serializers
    # path('', index, name='dogs'),
    path('', DogsView.as_view(), name='Dogs'),
    # this was our path before using rest framework and serializers
    # path('<int:pk>/', show, name='dog-detail')
    path('<int:pk>/', DogDetailView.as_view(), name='Dog-detail')
]