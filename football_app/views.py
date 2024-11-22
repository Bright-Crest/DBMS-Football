from django.shortcuts import render
from django.db.models import Sum

from collections import defaultdict
# from enum import Enum


# class Rank_type(Enum):
#     score = 1
#     goals = 2
#     assists = 3
#     red_card = 4
#     yellow_card = 5
#     fault = 6
#     tackling = 7


# def league_ranks(request, is_team, rank_type, leagues=None):
#     '''

#     Args:
#         request:
#         is_team (bool):
#         rank_type (Rank_type|int):
#         leagues (list):
#     '''

#     # if leagues is None:
#     #     leagues = Team.objects.values_list('team_league', flat=True).distinct()
#     # model = Team if is_team else Player
#     # league_rankings = {}
#     # for league in leagues:
#     #     objs = (
#     #         model.objects.filter(team__team_league=league)
#     #         .annotate(result=)
#     #     )

#     pass

from .models import Player, Team
from .models import Match


def match_results(request):
    '''
    比赛结果
    '''
    leagues = Match.objects.values_list('league_name', flat=True).distinct()
    match_results = {}
    for league in leagues:
        matches = Match.objects.filter(league_name=league).order_by('season_year', 'match_id')
        match_results[league] = matches
    return render(request, 'match_results.html', {'match_results': match_results})


# 球员榜

def top_scorers(request):
    '''
    球员进球榜
    '''
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
    '''
    球员助攻榜
    '''
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


def top_red_cards(request):
    '''
    球员红牌榜
    '''
    leagues = Team.objects.values_list('team_league', flat=True).distinct()
    league_rankings = {}
    for league in leagues:
        players = (
            Player.objects.filter(team__team_league=league)
            .annotate(total_red_cards=Sum('player_red_card'))
            .order_by('-total_red_cards')[:10]  # 取前10名
        )
        league_rankings[league] = players
    return render(request, 'top_red_cards.html', {'league_rankings': league_rankings})


def top_yellow_cards(request):
    '''
    球员黄牌榜
    '''
    leagues = Team.objects.values_list('team_league', flat=True).distinct()
    league_rankings = {}
    for league in leagues:
        players = (
            Player.objects.filter(team__team_league=league)
            .annotate(total_yellow_cards=Sum('player_yellow_card'))
            .order_by('-total_yellow_cards')[:10]  # 取前10名
        )
        league_rankings[league] = players
    return render(request, 'top_yellow_cards.html', {'league_rankings': league_rankings})


# 球队榜

def league_standings(request):
    '''
    球队积分榜
    '''
    leagues = Team.objects.values_list('team_league', flat=True).distinct()
    standings = {}
    for league in leagues:
        teams = (
            Team.objects.filter(team_league=league)
            .order_by('-team_score')[:10]  # 按积分降序排列，取前10名
        )
        standings[league] = teams
    return render(request, 'league_standings.html', {'standings': standings})


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

    return render(request, 'goal_ranking.html', {'standings': dict(standings)})


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

    return render(request, 'assist_ranking.html', {'standings': dict(standings)})


def red_card_ranking(request):
    """球队红牌榜"""
    # 获取所有球队
    teams = Team.objects.all()

    # 创建一个字典存储每个球队的总进球数
    team_red_cards = defaultdict(int)

    # 遍历所有球员，累计每个球队的进球数
    players = Player.objects.all()
    for player in players:
        if player.team:  # 确保球员关联了一个球队
            team_red_cards[player.team] += player.player_red_card

    # 将球队按进球数降序排序
    sorted_teams = sorted(team_red_cards.items(), key=lambda x: x[1], reverse=True)

    # 将球队按联赛分组
    standings = defaultdict(list)
    for team, red_cards in sorted_teams:
        standings[team.team_league].append({'team': team, 'total_red_cards': red_cards})

    return render(request, 'red_card_ranking.html', {'standings': dict(standings)})


def yellow_card_ranking(request):
    """球队黄牌榜"""
    # 获取所有球队
    teams = Team.objects.all()

    # 创建一个字典存储每个球队的总进球数
    team_yellow_cards = defaultdict(int)

    # 遍历所有球员，累计每个球队的进球数
    players = Player.objects.all()
    for player in players:
        if player.team:  # 确保球员关联了一个球队
            team_yellow_cards[player.team] += player.player_yellow_card

    # 将球队按进球数降序排序
    sorted_teams = sorted(team_yellow_cards.items(), key=lambda x: x[1], reverse=True)

    # 将球队按联赛分组
    standings = defaultdict(list)
    for team, yellow_cards in sorted_teams:
        standings[team.team_league].append({'team': team, 'total_yellow_cards': yellow_cards})

    return render(request, 'yellow_card_ranking.html', {'standings': dict(standings)})

    
def player_info(request):
    """球员信息页面"""
    # 获取所有球员信息
    players = Player.objects.all()
    return render(request, 'player_info.html', {'players': players})