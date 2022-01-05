#library/urls.py
from django.urls import path
# from .views import index, show
from .views import CatsView, CatsDetailView

urlpatterns = [
    # this was our path before using rest framework and serializers
    # path('', index, name='books'),
    path('', CatsView.as_view(), name='Cats'),
    # this was our path before using rest framework and serializers
    # path('<int:pk>/', show, name='book-detail')
    path('<int:pk>/', CatsDetailView.as_view(), name='Cats-detail')
]