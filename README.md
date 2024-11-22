# DBMS-Football

A homework project of NIS3351-Database which implements a DBMS managing football league info as a web app.

## 目录结构

```tree
DBMS-Football
 ┣ dbms_football ------------------------- // Django project
 ┃ ┣ settings.py ------------------------- // Django settings including MySQL settings
 ┃ ┣ urls.py
 ┣ football_app -------------------------- // the only Django app
 ┃ ┣ management
 ┃ ┃ ┗ commands
 ┃ ┃ ┃ ┗ update_team_and_player_stats.py - // `python manage.py update_team_and_player_stats` to run; 用于添加比赛数据后更新关联的球队球员数据
 ┃ ┣ migrations -------------------------- // `python manage.py migrate` to run; 在已创建的数据库中建表
 ┃ ┣ static ------------------------------ // jquery, Bootstrap and js
 ┃ ┣ templates --------------------------- // Django html templates
 ┃ ┃ ┣ assist_ranking.html --------------- // 球队助攻榜
 ┃ ┃ ┣ base_table.html
 ┃ ┃ ┣ footer.html ----------------------- // 页脚
 ┃ ┃ ┣ goal_ranking.html ----------------- // 球队进球榜
 ┃ ┃ ┣ home.html ------------------------- // 主页
 ┃ ┃ ┣ league_standings.html ------------- // 球队积分榜
 ┃ ┃ ┣ match_results.html ---------------- // 比赛结果
 ┃ ┃ ┣ navbar.html ----------------------- // 导航栏
 ┃ ┃ ┣ player_info.html ------------------ // 球员信息
 ┃ ┃ ┣ red_card_ranking.html ------------- // 球队红牌榜
 ┃ ┃ ┣ root.html ------------------------- // 根模板
 ┃ ┃ ┣ theme_toggler.html ---------------- // 亮暗主题切换组件
 ┃ ┃ ┣ top_assists.html ------------------ // 球员助攻榜
 ┃ ┃ ┣ top_red_cards.html ---------------- // 球员红牌榜
 ┃ ┃ ┣ top_scorers.html ------------------ // 球员进球榜
 ┃ ┃ ┣ top_yellow_cards.html ------------- // 球员黄牌榜
 ┃ ┃ ┗ yellow_card_ranking.html ---------- // 球队黄牌榜
 ┃ ┣ utils
 ┃ ┃ ┗ utils.py -------------------------- // utility functions
 ┃ ┣ middleware.py ----------------------- // Django中间件
 ┃ ┣ models.py --------------------------- // Django模型，即基本表
 ┃ ┣ urls.py
 ┃ ┣ views.py ---------------------------- // 视图函数，实现DBMS主要功能
 ┣ insert_test_data.sql ------------------ // insert a small amount of data to test
 ┣ manage.py
 ┣ NIS3351.sql
 ┣ README.md
 ┗ requirements.txt
```
