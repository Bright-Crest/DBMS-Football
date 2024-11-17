from django.urls import path
from . import views

app_name = "football_app"
urlpatterns = [
    path('top_scorers/', views.top_scorers, name='top_scorers'),
    path('top_assists/', views.top_assists, name='top_assists'),
    path('league_standings/', views.league_standings, name='league_standings'),
    path('match_results/', views.match_results, name='match_results'),
]
