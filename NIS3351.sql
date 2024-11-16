USE NIS3351;

-- 球队表
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
    team_fault INT,
    team_tackling INT,
    -- 备注 便于模糊查询
    team_index TEXT
);

-- 球员表
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
    player_fault INT,
    player_tackling INT,
    -- 备注 便于模糊查询
    player_index TEXT,
    -- 所属球队
    team_id INT NOT NULL,
    FOREIGN KEY(team_id) REFERENCES Teams(team_id)
);

-- 教练表
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

-- 比赛表
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

-- 参赛表
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
