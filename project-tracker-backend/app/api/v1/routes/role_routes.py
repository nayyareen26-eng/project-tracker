from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.role import Role 

router = APIRouter(
    prefix="/api/v1/roles",
    tags=["Roles"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally: 
        db.close()

@router.get("/")
def get_roles(db: Session = Depends(get_db)):
    return db.query(Role).all()