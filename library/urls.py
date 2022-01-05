from django.urls import path
# from .views import index, show
from .views import PlayersView, PlayersDetailView
urlpatterns = [
    # this was our path before using rest framework and serializers
    # path('', index, name='books'),
    path('', PlayersView.as_view(), name='Players'),
    # this was our path before using rest framework and serializes
    # path('<int:pk>/', show, name='book-detail')
    path('<int:pk>/', PlayersDetailView.as_view(), name='Players-detail')
]