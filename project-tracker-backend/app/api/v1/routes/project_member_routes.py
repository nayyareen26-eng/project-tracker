from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.project_member import ProjectMember
from app.schemas.project_member_schema import ProjectMemberCreate

router = APIRouter(
    prefix="/api/v1/project-members",
    tags=["Project Members"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_project_member(data: ProjectMemberCreate, db: Session = Depends(get_db)):
    member = ProjectMember(**data.dict())
    db.add(member)
    db.commit()
    db.refresh(member)
    return member

@router.get("/{project_id}")
def get_project_members(project_id: int, db: Session = Depends(get_db)):
    return db.query(ProjectMember).filter(
        ProjectMember.project_id == project_id
    ).all()
