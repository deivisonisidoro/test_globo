import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.infrastructure.database.connection import Base


@pytest.fixture(scope="function")
def in_memory_session():
    """
    Sets up an in-memory SQLite database session for testing.

    This fixture creates a new SQLite database in memory for each test,
    ensuring a clean state. It also tears down the database after the test
    is complete.

    Yields:
        Session: A SQLAlchemy session connected to the in-memory database.
    """
    engine = create_engine("sqlite:///:memory:")

    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()

    yield session

    session.close()
    Base.metadata.drop_all(bind=engine)
