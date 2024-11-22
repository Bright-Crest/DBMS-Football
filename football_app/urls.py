from django.urls import path
from . import views

app_name = "football_app"
urlpatterns = [
    path('match_results/', views.match_results, name='match_results'),
    path('top_scorers/', views.top_scorers, name='top_scorers'),
    path('top_assists/', views.top_assists, name='top_assists'),
    path('top_red_cards/', views.top_red_cards, name='top_red_cards'),
    path('top_yellow_cards/', views.top_yellow_cards, name='top_yellow_cards'),
    path('league_standings/', views.league_standings, name='league_standings'),
    path('goal_ranking/', views.goal_ranking, name='goal_ranking'),
    path('assist_ranking/', views.assist_ranking, name='assist_ranking'),
    path('red_card_ranking/', views.red_card_ranking, name='red_card_ranking'),
    path('yellow_card_ranking/', views.yellow_card_ranking, name='yellow_card_ranking'),
    path('player_info/', views.player_info, name='player_info'),
]
