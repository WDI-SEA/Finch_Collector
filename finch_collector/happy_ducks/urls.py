from  django.urls import path
from .views import DuckDetailView, DuckView

urlpatterns = [
    path('', DuckView.as_view(), name='Duck'),
    path('<int:pk>/', DuckDetailView.as_view(), name='Duck-detail')
]