from django.urls import path

from .views import SneakerView, SneakerDetailView

urlpatterns = [
    path('', SneakerView.as_view(), name='Sneakers'),
    path('<int:pk>/', SneakerDetailView.as_view(), name='Sneaker-detail')

]