import os
import dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

dotenv.load_dotenv()

# Postgres Database -> Example: postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}
DB_URL = os.getenv("DATABASE_URL")

"""
Creation of engine to stablish connection as well session for the transaction

Base is used for the creation the tables, and the database if not existing, it constains the metada used for it
"""
engine = create_engine(DB_URL, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine, autoflush=False)

# Generator used for dependency injection on FastAPI, self explanatory in code
def get_db():
    db = Session()
    
    try:
        yield db

    finally:
        db.close()