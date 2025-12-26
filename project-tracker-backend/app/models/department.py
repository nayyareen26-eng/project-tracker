from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base

class Department(Base):
    __tablename__ = "department"

    department_id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, nullable=False)
    department_name = Column(String(50), nullable=False)
    department_type = Column(String(50), nullable=False)
    
    teams = relationship("Team", back_populates="department")
