#library/urls.py
from django.urls import path
# from .views import index, show
from .views import CatsView, CatsDetailView
from .owner_views import Owner, OwnerDetail

urlpatterns = [
    path('owner', Owner.as_view(), name='owner'),
    path('owner/<int:pk>', OwnerDetail.as_view(), name='owner_detail'),
    path('cats', CatsView.as_view(), name='cats'),
    path('cats/<int:pk>', CatsDetailView.as_view(), name='cats_detail'),
    # this was our path before using rest framework and serializers
    # path('', index, name='books'),
    path('', CatsView.as_view(), name='cats')
    # this was our path before using rest framework and serializers
    # path('<int:pk>/', show, name='book-detail')
]