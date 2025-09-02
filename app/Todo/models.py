from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from database.db import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    todolist_name = Column(String)
    todo_list = Column(JSONB)

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="todo")
