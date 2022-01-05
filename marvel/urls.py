from django.urls import path

from .views.hero_views import HeroView, HeroDetailView
from .views.team_views import TeamView, TeamDetailView

urlpatterns = [
    path('heroes', HeroView.as_view(), name='heroes'),
    path('heroes/<int:pk>', HeroDetailView.as_view(), name='hero-detail'),
    path('teams', TeamView.as_view(), name='teams'),
    path('teams/<int:pk>', TeamDetailView.as_view(), name='team-detail')
]