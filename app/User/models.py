from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database.db import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)

    todo = relationship("Todos", back_populates="user", cascade="all, delete")