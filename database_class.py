from enum import Enum


class Rank_type(Enum):
    score = 1
    goals = 2
    assists = 3
    red_card = 4
    yellow_card = 5
    fault = 6
    tackling = 7


class Team:
    def __init_(
        self,
        team_id,
        team_name,
        team_league,
        team_index,
        team_score=0,
        team_goals=0,
        team_assists=0,
        team_red_card=0,
        team_yellow_card=0,
        team_fault=0,
        team_tackling=0,
    ):
        # 球队id
        self.team_id = team_id
        # 球队名称
        self.team_name = team_name
        # 球队所属联赛
        self.team_league = team_league
        # 球队分数 缺省为0
        self.team_score = team_score
        # 球队总进球数
        self.team_goals = team_goals
        # 球队总助攻数
        self.team_assists = team_assists
        # 球队红牌数
        self.team_red_card = team_red_card
        # 球队黄牌数
        self.team_yellow_card = team_yellow_card
        # 球队失误数
        self.team_fault = team_fault
        # 球队抢断数
        self.team_tackling = team_tackling
        # 球队备注 便于模糊查询
        self.team_index = team_index


class Player:
    def __init_(
        self,
        player_id,
        player_name,
        player_nationality,
        player_age,
        player_index,
        team_id,
        player_goals=0,
        player_assists=0,
        player_red_card=0,
        player_yellow_card=0,
        player_fault=0,
        player_tackling=0,
    ):
        # 球员id
        self.player_id = player_id
        # 球员名称
        self.player_name = player_name
        # 球员国籍
        self.player_nationality = player_nationality
        # 球员年龄
        self.player_age = player_age
        # 球员进球数
        self.player_goals = player_goals
        # 球员助攻数
        self.player_assists = player_assists
        # 球员红牌数
        self.player_red_card = player_red_card
        # 球员黄牌数
        self.player_yellow_card = player_yellow_card
        # 球员失误数
        self.player_fault = player_fault
        # 球员抢断数
        self.player_tackling = player_tackling
        # 球员备注 便于模糊查询
        self.player_index = player_index
        # 球员所属球队
        self.team_id = team_id


class Coach:
    def __init_(
        self, coach_id, coach_name, coach_nationality, coach_age, coach_index, team_id
    ):
        # 教练id
        self.coach_id = coach_id
        # 教练名称
        self.coach_name = coach_name
        # 教练国籍
        self.coach_nationality = coach_nationality
        # 教练年龄
        self.coach_age = coach_age
        # 教练备注 便于模糊查询
        self.coach_index = coach_index
        # 执教球队
        self.team_id = team_id
