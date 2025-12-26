from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.project import Project
from app.schemas.project_schemas import ProjectCreate, ProjectUpdate
router = APIRouter(
    prefix="/api/v1/projects",
    tags=["Projects"]
)

#create-project route
@router.post("/")
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db)
):
    new_project = Project(
        team_id=project.team_id,
        project_title=project.project_title,
        project_description=project.project_description,
        project_manager=project.project_manager,
        created_by=project.created_by
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return {
        "message": "Project created successfully",
        "project_id": new_project.project_id
    }

#viewall project route
@router.get("/list")
def view_all_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).all()

    return {
        "count": len(projects),
        "projects": projects
    }

#viewbyid project route
@router.get("/{project_id}")
def view_project_by_id(
    project_id: int,
    db: Session = Depends(get_db)
):
    project = db.query(Project).filter(
        Project.project_id == project_id
    ).first()

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project

#update project route
@router.post("/{project_id}")
def update_project(
    project_id: int,
    project: ProjectUpdate,
    db: Session = Depends(get_db)
):
    db_project = db.query(Project).filter(Project.project_id == project_id).first()

    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")

    if project.project_title is not None:
        db_project.project_title = project.project_title
    if project.project_description is not None:
        db_project.project_description = project.project_description
    if project.project_manager is not None:
        db_project.project_manager = project.project_manager
    if project.status is not None:
        db_project.status = project.status

    db.commit()
    db.refresh(db_project)

    return {
        "message": "Project updated successfully",
        "project_id": db_project.project_id
    }

#project delete route

@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db)
):
    project = db.query(Project).filter(Project.project_id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    db.delete(project)
    db.commit()

    return {
        "message": "Project deleted successfully",
        "project_id": project_id
    }