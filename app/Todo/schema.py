from pydantic import BaseModel
from typing import Any, Dict, Optional
import datetime

class TodoBase(BaseModel):
    todolist_name: str
    created_at: datetime.datetime
    todo_list: Dict[str, Any]

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    todo_name: Optional[str]
    todo_description: Optional[Dict[str, Any]]

class TodoOut(BaseModel):
    id: int
    todo_name: str
    todo_description: Dict[str, Any]
    user_id: int


    class Config:
        orm_mode = True