from sqlalchemy import Column, Integer, ForeignKey
from app.database.database import Base

class ProjectMember(Base):
    __tablename__ = "project_member"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("project.project_id"))
    user_id = Column(Integer, ForeignKey("user.user_id"))
    role_id = Column(Integer, ForeignKey("role.id"))