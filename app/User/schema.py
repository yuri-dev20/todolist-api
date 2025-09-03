from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    password: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str]
    password: Optional[str]

class UserOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True