from django.urls import path
from .views import SuperheroesView

urlpatterns = [
    path('', SuperheroesView.as_view(), name='Heroes'),
]