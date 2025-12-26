from pydantic import BaseModel

class RoleBase(BaseModel):
    role_type: str

class RoleResponse(RoleBase):
    id: int

    class Config:
        orm_mode = True