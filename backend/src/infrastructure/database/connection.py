import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", default="")

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """
    Dependency that provides a database session for each request.

    This function manages the lifecycle of a database session. It opens a
    new session and ensures that the session is closed after the request
    is completed.

    Yields:
        (SessionLocal): The database session object.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
