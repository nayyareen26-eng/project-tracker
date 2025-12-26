from sqlalchemy import Column, Integer, ForeignKey
from app.database.database import Base

class BoardProjectMapping(Base):
    __tablename__ = "board_project_mapping"

    id = Column(Integer, primary_key=True, index=True)
    board_id = Column(Integer, ForeignKey("boards.board_id"))
    project_id = Column(Integer, ForeignKey("projects.project_id"))
