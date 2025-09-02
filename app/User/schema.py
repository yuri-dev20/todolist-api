from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    password: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: str

class UserOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True