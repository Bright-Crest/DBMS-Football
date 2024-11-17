from django.contrib import admin
from .models import Team, Player, Coach, Match, Participation

# 自定义 Team 模型的显示方式
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'team_league', 'team_score', 'team_goals', 'team_assists', 'team_red_card', 'team_yellow_card', 'team_fault', 'team_tackling')
    search_fields = ('team_name', 'team_league')  # 支持模糊搜索

# 自定义 Player 模型的显示方式
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'team', 'player_goals', 'player_assists', 'player_red_card', 'player_yellow_card', 'player_fault', 'player_tackling')
    search_fields = ('player_name', 'team__team_name')  # 支持球员名和球队名的模糊搜索
    list_filter = ('team',)  # 按球队筛选

# 自定义 Coach 模型的显示方式
class CoachAdmin(admin.ModelAdmin):
    list_display = ('coach_name', 'team', 'coach_age')
    search_fields = ('coach_name', 'team__team_name')  # 支持教练名和球队名的模糊搜索
    list_filter = ('team',)  # 按球队筛选

# 自定义 Match 模型的显示方式
class MatchAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'away_team', 'home_team_goals', 'away_team_goals', 'league_name', 'season_year')
    search_fields = ('home_team__team_name', 'away_team__team_name', 'league_name', 'season_year')
    list_filter = ('league_name', 'season_year')  # 按联赛名称和赛季筛选

# 自定义 Participation 模型的显示方式
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('player', 'match', 'goals', 'assists', 'red_cards', 'yellow_cards')
    search_fields = ('player__player_name', 'match__home_team__team_name', 'match__away_team__team_name')
    list_filter = ('match', 'player')  # 按比赛和球员筛选

# 注册模型到 admin
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Participation, ParticipationAdmin)
