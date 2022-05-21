import string
from pydantic import BaseModel
class HomeAway(BaseModel):
    homeTeamName: str
    awayTeamName: str