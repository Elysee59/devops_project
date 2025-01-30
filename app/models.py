from sqlalchemy import Column, Integer, String
from app.database import Base

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    team_a = Column(String, index=True)
    team_b = Column(String, index=True)
    date = Column(String)
    location = Column(String)
