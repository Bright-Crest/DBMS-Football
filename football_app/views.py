from django.shortcuts import render
from django.db.models import Sum
from .models import Player, Team
from collections import defaultdict


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
    for league in leagues:
        matches = Match.objects.filter(league_name=league).order_by('season_year', 'match_id')
        match_results[league] = matches
    return render(request, 'match_results.html', {'match_results': match_results})


def goal_ranking(request):
    """球队进球榜"""
    # 获取所有球队
    teams = Team.objects.all()

    # 创建一个字典存储每个球队的总进球数
    team_goals = defaultdict(int)

    # 遍历所有球员，累计每个球队的进球数
    players = Player.objects.all()
    for player in players:
        if player.team:  # 确保球员关联了一个球队
            team_goals[player.team] += player.player_goals

    # 将球队按进球数降序排序
    sorted_teams = sorted(team_goals.items(), key=lambda x: x[1], reverse=True)

    # 将球队按联赛分组
    standings = defaultdict(list)
    for team, goals in sorted_teams:
        standings[team.team_league].append({'team': team, 'total_goals': goals})

    return render(request, 'goal_ranking.html', {'standings': standings})

def assist_ranking(request):
    """球队助攻榜"""
    # 获取所有球队
    teams = Team.objects.all()

    # 创建一个字典存储每个球队的总助攻数
    team_assists = defaultdict(int)

    # 遍历所有球员，累计每个球队的助攻数
    players = Player.objects.all()
    for player in players:
        if player.team:  # 确保球员关联了一个球队
            team_assists[player.team] += player.player_assists

    # 将球队按助攻数降序排序
    sorted_teams = sorted(team_assists.items(), key=lambda x: x[1], reverse=True)

    # 将球队按联赛分组
    standings = defaultdict(list)
    for team, assists in sorted_teams:
        standings[team.team_league].append({'team': team, 'total_assists': assists})

    return render(request, 'assist_ranking.html', {'standings': standings})