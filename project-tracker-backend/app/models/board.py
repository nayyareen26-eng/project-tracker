from sqlalchemy import Column, Integer, String, DateTime
from app.database.database import Base

class Board(Base):
    __tablename__ = "board"

    board_id = Column(Integer, primary_key=True, index=True)
    board_title = Column(String(20))
    sprint_start_date = Column(DateTime)
    sprint_end_date = Column(DateTime)
    board_short_description = Column(String(50))
