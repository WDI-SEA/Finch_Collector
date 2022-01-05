#library/urls.py
from django.urls import path
# from .views import index, show
from .views import TradingCardDetailView, TradingCardsView

urlpatterns = [
    # this was our path before using rest framework and serializers
    # path('', index, name='books'),
    path('', TradingCardsView.as_view(), name='Books'),
    # this was our path before using rest framework and serializers
    # path('<int:pk>/', show, name='book-detail')
    path('<int:pk>/', TradingCardDetailView.as_view(), name='Book-detail')
]