from django.urls import path
from movies import views

urlpatterns = [
    path('', views.MoviesView.as_view(), name="movies"),
    path('<int:pk>', views.MovieDetailView.as_view(), name="movie")
]
