from django.shortcuts import render
from django.db.models import Sum
from .models import Player, Team


def top_scorers(request):
    leagues = Team.objects.values_list('team_league', flat=True).distinct()
    league_rankings = {}
    for league in leagues:
        players = (
            Player.objects.filter(team__team_league=league)
            .annotate(total_goals=Sum('player_goals'))
            .order_by('-total_goals')[:10]  # 取前10名
        )
        league_rankings[league] = players
    return render(request, 'top_scorers.html', {'league_rankings': league_rankings})


def top_assists(request):
    leagues = Team.objects.values_list('team_league', flat=True).distinct()
    league_rankings = {}
    for league in leagues:
        players = (
            Player.objects.filter(team__team_league=league)
            .annotate(total_assists=Sum('player_assists'))
            .order_by('-total_assists')[:10]  # 取前10名
        )
        league_rankings[league] = players
    return render(request, 'top_assists.html', {'league_rankings': league_rankings})


def league_standings(request):
    leagues = Team.objects.values_list('team_league', flat=True).distinct()
    standings = {}
    for league in leagues:
        teams = (
            Team.objects.filter(team_league=league)
            .order_by('-team_score')[:10]  # 按积分降序排列，取前10名
        )
        standings[league] = teams
    return render(request, 'league_standings.html', {'standings': standings})


from .models import Match


def match_results(request):
    leagues = Match.objects.values_list('league_name', flat=True).distinct()
    match_results = {}
    # BUG: 由于比赛有两支队伍，比赛被输出两次
    for league in leagues:
        matches = Match.objects.filter(league_name=league).order_by('season_year', 'match_id')
        match_results[league] = matches
    return render(request, 'match_results.html', {'match_results': match_results})
