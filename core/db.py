from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()
database_url = os.getenv('DATABASE_URL')

engine = create_engine(database_url)
sessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

