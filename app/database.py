from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL connection URL
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:stringcode@localhost/user_fastapi_db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgrefega@localhost/blog-fastapi"

# Connect to PostgreSQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
