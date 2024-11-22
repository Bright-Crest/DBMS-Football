from django.db import models


# 球队表
class Team(models.Model):
    team_id = models.AutoField(primary_key=True)  # 主键，自动递增
    team_name = models.CharField(max_length=100, unique=True)  # 球队名称
    team_league = models.CharField(max_length=100)  # 所属联赛
    team_score = models.IntegerField(default=0)  # 球队得分
    team_goals = models.IntegerField(default=0)  # 球队进球数
    team_assists = models.IntegerField(default=0)  # 助攻数
    team_red_card = models.IntegerField(default=0)  # 红牌数
    team_yellow_card = models.IntegerField(default=0)  # 黄牌数


    def __str__(self):
        return self.team_name


# 球员表
class Player(models.Model):
    player_id = models.AutoField(primary_key=True)  # 主键，自动递增
    player_name = models.CharField(max_length=100)  # 球员姓名
    player_nationality = models.CharField(max_length=100, null=True, blank=True)  # 国籍
    player_age = models.IntegerField(null=True, blank=True)  # 年龄
    player_goals = models.IntegerField(default=0)  # 进球数
    player_assists = models.IntegerField(default=0)  # 助攻数
    player_red_card = models.IntegerField(default=0)  # 红牌数
    player_yellow_card = models.IntegerField(default=0)  # 黄牌数
    team = models.ForeignKey(Team, on_delete=models.CASCADE)  # 外键，所属球队

    def __str__(self):
        return self.player_name


# 教练表
class Coach(models.Model):
    coach_id = models.AutoField(primary_key=True)  # 主键，自动递增
    coach_name = models.CharField(max_length=100)  # 教练姓名
    coach_nationality = models.CharField(max_length=100, null=True, blank=True)  # 国籍
    coach_age = models.IntegerField(null=True, blank=True)  # 年龄
    team = models.ForeignKey(Team, on_delete=models.CASCADE)  # 外键，执教球队

    def __str__(self):
        return self.coach_name


# 比赛表
class Match(models.Model):
    match_id = models.AutoField(primary_key=True)  # 主键，自动递增
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')  # 主队
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')  # 客队
    home_team_goals = models.IntegerField(default=0)  # 主队进球数
    away_team_goals = models.IntegerField(default=0)  # 客队进球数
    league_name = models.CharField(max_length=100)  # 联赛名称
    season_year = models.CharField(max_length=9)  # 联赛赛季
    is_completed = models.BooleanField(default=False)  # 标记比赛是否完赛，默认未完赛

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} ({self.league_name}, {self.season_year})"


# 参赛表
class Participation(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)  # 外键，关联球员
    match = models.ForeignKey(Match, on_delete=models.CASCADE)  # 外键，关联比赛
    goals = models.IntegerField(default=0)  # 进球数
    assists = models.IntegerField(default=0)  # 助攻数
    red_cards = models.IntegerField(default=0)  # 红牌数
    yellow_cards = models.IntegerField(default=0)  # 黄牌数

    class Meta:
        unique_together = ('player', 'match')  # 联合主键
        ordering = ['-goals', '-assists']  # 按进球和助攻降序排序

    def __str__(self):
        return f"{self.player} in {self.match}"
