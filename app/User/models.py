from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database.db import Base

"""
    The class inherits from Base enabling it the table to be created

    inside it we have the table name and a relationship for it's use in the ORM
"""
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)

    todo = relationship("Todos", back_populates="user", cascade="all, delete")