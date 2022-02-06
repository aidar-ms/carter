from config import base
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

def get_session():
    engine = create_engine(base.SQLALCHEMY_DATABASE_URI)
    Session = sessionmaker(bind=engine)
    return Session()

# Base model
Base = declarative_base()
