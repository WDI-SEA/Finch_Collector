#library/urls.py
from django.urls import path
# from .views import index, show
from .views import AnimeView, AnimeDetailView

urlpatterns = [
    # this was our path before using rest framework and serializers
    # path('', index, name='books'),
    path('', AnimeView.as_view(), name='Anime'),
    # this was our path before using rest framework and serializers
    # path('<int:pk>/', show, name='book-detail')
    path('<int:pk>/', AnimeDetailView.as_view(), name='Anime-detail')
]