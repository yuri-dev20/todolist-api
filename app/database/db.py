import os
import dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

dotenv.load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

engine = create_engine(DB_URL, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine, autoflush=False)

def get_db():
    db = Session()
    
    try:
        yield db

    finally:
        db.close()