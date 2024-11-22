from django.core.management.base import BaseCommand
from football_app.models import Match, Team, Participation, Player

class Command(BaseCommand):
    help = "更新球队积分和球员的进球、助攻等信息"

    def handle(self, *args, **kwargs):
        # 更新球队积分
        matches = Match.objects.all()
        for match in matches:
            home_team = match.home_team
            away_team = match.away_team

            # 根据比赛结果更新积分
            if match.home_team_goals > match.away_team_goals:
                home_team.team_score += 3
            elif match.home_team_goals < match.away_team_goals:
                away_team.team_score += 3
            else:
                home_team.team_score += 1
                away_team.team_score += 1

            # 保存球队积分更新
            home_team.save()
            away_team.save()

        # 更新球员数据
        participations = Participation.objects.all()
        for participation in participations:
            player = participation.player

            # 累加球员表现数据
            player.player_goals += participation.goals
            player.player_assists += participation.assists
            player.player_red_card += participation.red_cards
            player.player_yellow_card += participation.yellow_cards

            # 保存球员数据更新
            player.save()

        self.stdout.write(self.style.SUCCESS("球队积分和球员数据更新完成！"))
