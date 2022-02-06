from config import base
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


engine = create_engine(base.SQLALCHEMY_DATABASE_URI)

# Base model
Base = declarative_base()
