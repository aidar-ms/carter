from config import base
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

def get_session():
    engine = create_engine(base.DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return Session()

# Base model
Base = declarative_base()
