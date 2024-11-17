USE NIS3351;

INSERT INTO football_app_team (team_name, team_league, team_score, team_goals, team_assists, team_red_card, team_yellow_card, team_fault, team_tackling) VALUES ("team1", "league1", 3, 0, 0, 0, 0, 0, 0);
INSERT INTO football_app_team (team_name, team_league, team_score, team_goals, team_assists, team_red_card, team_yellow_card, team_fault, team_tackling) VALUES ("team2", "league1", 1, 0, 0, 0, 0, 0, 0);
INSERT INTO football_app_team (team_name, team_league, team_score, team_goals, team_assists, team_red_card, team_yellow_card, team_fault, team_tackling) VALUES ("team3", "league1", 2, 0, 0, 0, 0, 0, 0);
INSERT INTO football_app_team (team_name, team_league, team_score, team_goals, team_assists, team_red_card, team_yellow_card, team_fault, team_tackling) VALUES ("team4", "league2", 1, 0, 0, 0, 0, 0, 0);
INSERT INTO football_app_team (team_name, team_league, team_score, team_goals, team_assists, team_red_card, team_yellow_card, team_fault, team_tackling) VALUES ("team5", "league2", 3, 0, 0, 0, 0, 0, 0);
INSERT INTO football_app_team (team_name, team_league, team_score, team_goals, team_assists, team_red_card, team_yellow_card, team_fault, team_tackling) VALUES ("team6", "league2", 2, 0, 0, 0, 0, 0, 0);

INSERT INTO football_app_player (player_name, player_goals, player_assists, player_red_card, player_yellow_card, player_fault, player_tackling, team_id) VALUES ("player1", 0, 0, 0, 0, 0, 0, 1);
INSERT INTO football_app_player (player_name, player_goals, player_assists, player_red_card, player_yellow_card, player_fault, player_tackling, team_id) VALUES ("player2", 0, 0, 0, 0, 0, 0, 1);
INSERT INTO football_app_player (player_name, player_goals, player_assists, player_red_card, player_yellow_card, player_fault, player_tackling, team_id) VALUES ("player3", 0, 0, 0, 0, 0, 0, 2);
INSERT INTO football_app_player (player_name, player_goals, player_assists, player_red_card, player_yellow_card, player_fault, player_tackling, team_id) VALUES ("player4", 0, 0, 0, 0, 0, 0, 2);
INSERT INTO football_app_player (player_name, player_goals, player_assists, player_red_card, player_yellow_card, player_fault, player_tackling, team_id) VALUES ("player5", 0, 0, 0, 0, 0, 0, 4);
INSERT INTO football_app_player (player_name, player_goals, player_assists, player_red_card, player_yellow_card, player_fault, player_tackling, team_id) VALUES ("player6", 0, 0, 0, 0, 0, 0, 4);
INSERT INTO football_app_player (player_name, player_goals, player_assists, player_red_card, player_yellow_card, player_fault, player_tackling, team_id) VALUES ("player7", 0, 0, 0, 0, 0, 0, 5);
INSERT INTO football_app_player (player_name, player_goals, player_assists, player_red_card, player_yellow_card, player_fault, player_tackling, team_id) VALUES ("player8", 0, 0, 0, 0, 0, 0, 5);

INSERT INTO football_app_match (home_team_goals, away_team_goals, league_name, season_year, away_team_id, home_team_id) VALUES (2, 1, "league1", "2024", 1, 2);
INSERT INTO football_app_match (home_team_goals, away_team_goals, league_name, season_year, away_team_id, home_team_id) VALUES (2, 1, "league2", "2024", 4, 5);

INSERT INTO football_app_participation (goals, assists, red_cards, yellow_cards, match_id, player_id) VALUES (2, 0, 0, 0, 1, 1);
INSERT INTO football_app_participation (goals, assists, red_cards, yellow_cards, match_id, player_id) VALUES (0, 2, 0, 0, 1, 2);
INSERT INTO football_app_participation (goals, assists, red_cards, yellow_cards, match_id, player_id) VALUES (1, 0, 0, 0, 1, 3);
INSERT INTO football_app_participation (goals, assists, red_cards, yellow_cards, match_id, player_id) VALUES (0, 1, 0, 0, 1, 4);
INSERT INTO football_app_participation (goals, assists, red_cards, yellow_cards, match_id, player_id) VALUES (1, 1, 0, 0, 2, 5);
INSERT INTO football_app_participation (goals, assists, red_cards, yellow_cards, match_id, player_id) VALUES (1, 1, 0, 0, 2, 6);
INSERT INTO football_app_participation (goals, assists, red_cards, yellow_cards, match_id, player_id) VALUES (0, 1, 0, 0, 2, 7);
INSERT INTO football_app_participation (goals, assists, red_cards, yellow_cards, match_id, player_id) VALUES (1, 0, 0, 0, 2, 8);