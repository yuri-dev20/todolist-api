from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from database.db import Base

import datetime

"""
    The only difference here from the other is the existence of the FK 'user_id' since it's a relationship 1:N

    A todo have only one user but a user can have many todos
"""
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    todo_name = Column(String)
    todo_description = Column(JSONB)

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="todo")
