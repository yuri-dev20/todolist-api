from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(user_password: str, stored_hashed_password):
    return bcrypt_context.verify(user_password, stored_hashed_password)

def get_password_hash(password: str):
    return bcrypt_context.hash(password)