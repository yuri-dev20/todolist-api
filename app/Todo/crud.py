from sqlalchemy.orm import Session
from .models import Todo
from .schema import TodoCreate, TodoUpdate
from User.crud import verify_user_id

from fastapi import HTTPException, status

"""
    TODO: JWT será implementado e esse código assim como outros serão refatorados
"""

# Função auxiliar para descobrir se existe Todo com determinado id
def verify_todo_id(db: Session, todo_id: int):
    todo = db.get(Todo, todo_id)
    if todo is None:
        return None
    
    return todo

# CRUD
# Create a todo
def crud_create_todo(db: Session, new_todo: TodoCreate, user_id: int):
    # O Pydantic permite a conversão para um dict Python com model_dump
    new_todo_data = new_todo.model_dump()

    user = verify_user_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário com ID {user_id} não encontrado!. Todo não foi criado.")

    todo = Todo(**new_todo_data, user_id=user_id)
    
    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo

# Read 'n' todos
def crud_read_todos(db: Session, limit: int = None):
    if limit is not None:
        return db.query(Todo).limit(limit).all()
    
    return db.query(Todo).all()
# Read a todo
def crud_read_todo(db: Session, todo_id: int):
    todo = verify_todo_id(db, todo_id)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo com {todo_id} não existe.")
    
    return todo

# Update a todo
def crud_update_todo(db: Session, todo_id: int, user_id: int, new_todo_data: TodoUpdate):
    todo = verify_todo_id(db, todo_id)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo com {todo_id} não existe.")
    
    user = verify_user_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário com ID {user_id} não encontrado!. Todo não pode ser alterado.")
    elif user.id != todo.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail=f"Usuário com ID {user_id} não é dono do Todo com nome {todo.todo_name} e id {todo.id}")
    
    if new_todo_data.todo_name is not None:
        todo.todo_name = new_todo_data.todo_name
    if new_todo_data.todo_description is not None:
        todo.todo_description = new_todo_data.todo_description

    db.commit()
    db.refresh(todo)

    return todo

# Delete a todo
def crud_delete_todo(db: Session, todo_id: int, user_id: int):
    todo = verify_todo_id(db, todo_id)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo com {todo_id} não existe.")
    
    user = verify_user_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário com ID {user_id} não encontrado!. Não foi possivel excluir o Todo.")
    
    if user.id != todo.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail=f"Usuário com ID {user_id} não é dono do Todo com nome {todo.todo_name} e id {todo.id}")

    db.delete(todo)
    db.commit()
    
    return todo