from pydantic import BaseModel
from datetime import datetime

class BoardCreate(BaseModel):
    project_id: int
    board_title: str
    sprint_start_date: datetime
    sprint_end_date: datetime
    board_short_description: str
