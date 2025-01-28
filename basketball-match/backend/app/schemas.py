from pydantic import BaseModel

class MatchBase(BaseModel):
    team_a: str
    team_b: str
    date: str
    location: str

class MatchCreate(MatchBase):
    pass

class Match(MatchBase):
    id: int

    class Config:
        orm_mode = True
