from django.urls import path
from .views import BagsView, BagDetailView

urlpatterns = [
    path('', BagsView.as_view(), name='Bags'),
    path('<int:pk>/', BagDetailView.as_view(), name='Bag-detail')
]