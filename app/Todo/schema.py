from pydantic import BaseModel
from typing import Any, Dict

class TodoBase(BaseModel):
    todolist_name: str
    todo_list: Dict[str, Any]

class TodoCreate(TodoBase):
    user_id: int

class TodoUpdate(BaseModel):
    todolist_name: str | None
    todo_list: Dict[str, Any] | None

class TodoOut(BaseModel):
    id: int
    todolist_name: str
    todo_list: Dict[str, Any]
    user_id: int


    class Config:
        orm_mode = True