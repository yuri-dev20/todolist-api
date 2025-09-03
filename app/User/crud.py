from sqlalchemy.orm import Session
from .models import User
from .schema import UserCreate, UserUpdate
from auth.service import get_password_hash

from fastapi import HTTPException, status

# Função auxiliar para descobrir se existe usuário com determinado id
def verify_user_id(db: Session, user_id: int):
    user = db.get(User, user_id)
    if user is None:
        return None
    
    return user

# CRUD
# CREATE a user
def crud_create_user(db: Session, new_user: UserCreate):
    user_verify = db.query(User).filter(User.name == new_user.name).first()
    if user_verify:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Um usuário com este nome já existe. Tente novamente com um nome diferente.")

    # Conversão Pydantic para dict Python
    new_user_data = new_user.model_dump()

    # '**' desempacota
    user = User(**new_user_data)
    user.password = get_password_hash(user.password)

    db.add(user) # Adciona o objeto a sessão do banco
    db.commit() # Faz o commit ou salva as alterações no banco
    db.refresh(user) # Sincroniza o objeto com o estado mais recente do banco pós commit

# READ n users
def crud_get_users(db: Session, limit: int = None):
    if limit is not None:
        return db.query(User).limit(limit).all()
    
    return db.query(User).all()

# READ a user
def crud_get_user(db: Session, user_id: int):
    user = verify_user_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário com ID {user_id} não encontrado!")
    
    return user

# UPDATE a user
def crud_update_user(db: Session, user_id: int, update_user_data: UserUpdate):
    user = verify_user_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário com ID {user_id} não encontrado!")
    
    if update_user_data.name is not None:
        user.name = update_user_data.name

    if update_user_data.password is not None:
        user.password = get_password_hash(update_user_data.password)

    db.commit()
    db.refresh(user)

    return user

# DELETE a user
def crud_delete_user(db: Session, user_id: int):
    user = verify_user_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário com ID {user_id} não encontrado!")
    
    db.delete(user)
    db.commit()

    return user