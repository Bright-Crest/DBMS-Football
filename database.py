import database_class
import pymysql


# 创建python和MySQL连接
def create_connection():
    conn = pymysql.connect(
        host="localhost",  # 根据你的数据库主机设置
        user="root",  # MySQL用户名#
        password="daerwen",# MySQL密码
        database="NIS3351",  # 数据库名称
    )
    return conn

# 创建球队 输入Team类 返回是否创建成功 特殊情况返回-1
def create_team(new_team : database_class.Team) :

# 创建球员 输入Player类 返回是否创建成功 特殊情况返回-1
def create_player(new_player: database_class.Player) :

# 创建教练 输入Coach类 返回是否创建成功 特殊情况返回-1
def create_coach(new_coach : database_class.Coach) :

# 修改球队 全字段替换 输入Team类 返回是否修改成功 特殊情况返回-1
def change_team(new_team : database_class.Team) :

# 修改球员 全字段替换 输入Player类 返回是否修改成功 特殊情况返回-1
def change_player(new_player : database_class.Player) :

# 修改球员 全字段替换 输入Coach类 返回是否修改你成功 特殊情况返回-1
def change_coach(new_coach : database_class.Coach) :

# 查询球队 全字段查询 输入字符串 返回球队id 特殊情况返回-1
def search_team(content : str) :

# 查询球员 全字段查询 输入字符串 返回球员id 特殊情况返回-1
def search_player(content : str) :

# 查询教练 全字段查询 输入字符串 返回教练id 特殊情况返回-1
def search_coach(content : str) :

# 全字段查询 输入字符串 返回球员/球队/教练id 和 id类型 特殊情况返回-1 -1
def search_all(content : str) :

# 查询球队榜单 返回球队id list 特殊情况返回NULL
def search_team_rank(rank_type : Rank_type) :

# 查询球员榜单 返回球员id list 特殊情况返回NULL
def search_player_rank(rank_type: Rank_type) :

# 删除球队 输入球队id 返回是否删除成功 特殊情况返回-1
def delete_team(team_id : int) :

# 删除球员 输入球员id 返回是否删除成功 特殊情况返回-1
def delete_player(player_id : int) :

# 删除教练 输入教练id 返回是否删除成功 特殊情况返回-1
def delete_coach(coach_id : int) :

# 显示球队信息 输入球队id 返回Team类
def show_team(team_id: int) :

# 显示球员信息 输入球员id 返回Player类
def show_player(player_id: int) :

# 显示教练信息 输入教练id 返回Coach类
def show_coach(coach_id: int) :

# 根据名称定位id 输入类型：1 球队 2 球员 3 教练
def name_to_id(name : str, type : int) -> int :

# 根据id定位名称 输入类型：1 球队 2 球员 3 教练
def id_to_name(id : int, type: int) -> int :