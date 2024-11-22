from typing import Iterable
from django.db import models


# 球队表
class Team(models.Model):
    '''
    CREATE TABLE Teams (
        -- 球队id 主键唯一标识
        team_id INT AUTO_INCREMENT PRIMARY KEY,
        -- 球队基本信息
        team_name VARCHAR(100) NOT NULL,
        team_league VARCHAR(100) NOT NULL,
        -- 球队赛场表现
        team_score INT,
        team_goals INT,
        team_assists INT,
        team_red_card INT,
        team_yellow_card INT,
    );
    '''

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
    '''
    CREATE TABLE Players (
        -- 球员id 主键唯一标识
        player_id INT AUTO_INCREMENT PRIMARY KEY,
        -- 球员个人信息
        player_name VARCHAR(100) NOT NULL,
        player_nationality VARCHAR(100),
        player_age INT,
        -- 球员赛场表现
        player_goals INT,
        player_assists INT,
        player_red_card INT,
        player_yellow_card INT,
        -- 所属球队
        team_id INT NOT NULL,
        FOREIGN KEY(team_id) REFERENCES Teams(team_id)
    );
    '''

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
    '''
    CREATE TABLE Coaches (
        -- 教练id 主键唯一标识
        coach_id INT AUTO_INCREMENT PRIMARY KEY,
        -- 教练个人信息
        coach_name VARCHAR(100) NOT NULL,
        coach_nationality VARCHAR(100),
        coach_age INT,
        -- 备注 便于模糊查询
        coach_index TEXT,
        -- 执教球队
        team_id INT NOT NULL,
        FOREIGN KEY(team_id) REFERENCES Teams(team_id)
    );
    '''

    coach_id = models.AutoField(primary_key=True)  # 主键，自动递增
    coach_name = models.CharField(max_length=100)  # 教练姓名
    coach_nationality = models.CharField(max_length=100, null=True, blank=True)  # 国籍
    coach_age = models.IntegerField(null=True, blank=True)  # 年龄
    team = models.ForeignKey(Team, on_delete=models.CASCADE)  # 外键，执教球队

    def __str__(self):
        return self.coach_name


# 比赛表
class Match(models.Model):
    '''
    CREATE TABLE Matches (
        -- 比赛id 主键唯一标识
        match_id INT AUTO_INCREMENT PRIMARY KEY,
        -- 主队id，外键关联到Teams表
        home_team_id INT NOT NULL,
        -- 客队id，外键关联到Teams表
        away_team_id INT NOT NULL,
        -- 主队进球数
        home_team_goals INT NOT NULL DEFAULT 0,
        -- 客队进球数
        away_team_goals INT NOT NULL DEFAULT 0,
        -- 所属联赛名称
        league_name VARCHAR(100) NOT NULL,
        -- 所属联赛赛季
        season_year VARCHAR(9) NOT NULL,
        -- 添加外键约束，确保数据一致性
        CONSTRAINT fk_home_team FOREIGN KEY (home_team_id) REFERENCES Teams(team_id),
        CONSTRAINT fk_away_team FOREIGN KEY (away_team_id) REFERENCES Teams(team_id)
    );
    '''

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
    '''
    CREATE TABLE Participation (
        -- 球员id，外键关联到 Players 表
        player_id INT NOT NULL,
        -- 比赛id，外键关联到 Matches 表
        match_id INT NOT NULL,
        -- 球员在该比赛中的表现数据
        goals INT NOT NULL DEFAULT 0, -- 进球数
        assists INT NOT NULL DEFAULT 0, -- 助攻数
        red_cards INT NOT NULL DEFAULT 0, -- 红牌数
        yellow_cards INT NOT NULL DEFAULT 0, -- 黄牌数
        -- 联合主键
        PRIMARY KEY (player_id, match_id),
        -- 添加外键约束
        CONSTRAINT fk_player FOREIGN KEY (player_id) REFERENCES Players(player_id),
        CONSTRAINT fk_match FOREIGN KEY (match_id) REFERENCES Matches(match_id)
    );
    '''

    player = models.ForeignKey(Player, on_delete=models.CASCADE)  # 外键，关联球员
    match = models.ForeignKey(Match, on_delete=models.CASCADE)  # 外键，关联比赛
    goals = models.IntegerField(default=0)  # 进球数
    assists = models.IntegerField(default=0)  # 助攻数
    red_cards = models.IntegerField(default=0)  # 红牌数
    yellow_cards = models.IntegerField(default=0)  # 黄牌数

    class Meta:
        # 联合主键。由于Django目前不支持定义联合主键，此模型以自增的id为形式主键，
        # 这里定义unique_together相当于mysql里的联合主键
        unique_together = ('player', 'match')  
        ordering = ['-goals', '-assists']  # 按进球和助攻降序排序

    def __str__(self):
        return f"{self.player} in {self.match}"
