# #library/urls.py
# from django.urls import path
# # from .views import index, show
from .views import SightingsView, SightingDetailView

# urlpatterns = [
#     # this was our path before using rest framework and serializers
#     # path('', index, name='books'),
#     # path('', BooksView.as_view(), name='Books'),

#     # # this was our path before using rest framework and serializers
#     # # path('<int:pk>/', show, name='book-detail')
#     # path('<int:pk>/', BookDetailView.as_view(), name='Book-detail')
#     # first_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', SightingsView.as_view(), name='books'),
    path('<int:pk>/', SightingDetailView.as_view(), name='Sighting-detail')
]
