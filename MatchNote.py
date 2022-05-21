from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class MatchNote(BaseModel):
    is_cup: int 
    home_team_history_goal: int
    away_team_history_goal: int 
    home_team_history_opponent_goal: int
    away_team_history_opponent_goal :int
    home_team_history_rating :float
    away_team_history_rating :float
    home_team_history_opponent_rating :float
    away_team_history_opponent_rating :float