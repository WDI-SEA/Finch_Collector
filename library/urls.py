from django.urls import path
from .views import DogsView, DogsDetailView

urlpatterns = [
    path('', DogsView.as_view(), name='Dogs'),
    path('<int:pk>/', DogsDetailView.as_view(), name='Dog-Detail')
]




