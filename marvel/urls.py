from django.urls import path

from .views.hero_views import Heroes, HeroDetail
from .views.team_views import Teams, TeamDetail

urlpatterns = [
    path('heroes', Heroes.as_view(), name='heroes'),
    path('heroes/<int:pk>', HeroDetail.as_view(), name='hero-detail'),
    path('teams', Teams.as_view(), name='teams'),
    path('teams/<int:pk>', TeamDetail.as_view(), name='team-detail')
]