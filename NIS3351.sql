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
