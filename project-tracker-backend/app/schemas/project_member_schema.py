from pydantic import BaseModel

class ProjectMemberCreate(BaseModel):
    project_id: int
    user_id: int
    role_id: int