import os
from contextlib import contextmanager
from typing import Any, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.infrastructure.database.connection import Base, get_db
from src.presentation.main import app


@contextmanager
@pytest.fixture(scope="function")
def in_memory_session() -> Generator[pytest.Session, None, None]:
    """
    Sets up an in-memory SQLite database session for testing.

    This fixture creates a new SQLite database in memory for each test,
    ensuring a clean state. It also tears down the database after the test
    is complete.

    Yields:
        Session: A SQLAlchemy session connected to the in-memory database.
    """
    SQL_ALCHEMY_DATABASE_URL = "sqlite:///./test.db"
    engine = create_engine(
        SQL_ALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    SessionTesting = sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )

    session = SessionTesting()
    Base.metadata.create_all(engine)

    try:
        yield session
    finally:
        session.close()
        session.rollback()
        Base.metadata.drop_all(bind=engine)
        engine.dispose()

        try:
            os.remove("test.db")
        except FileNotFoundError:
            pass


@pytest.fixture(scope="function")
def client(
    in_memory_session: pytest.Session,
) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the in-memory database.

    This fixture overrides the `get_db` dependency with the in-memory session,
    allowing tests to interact with the API as if it were using a real database.

    Args:
        app (FastAPI): The FastAPI application instance.
        in_memory_session (SessionTesting): The in-memory database session.

    Yields:
        TestClient: A FastAPI test client instance.
    """
    app.dependency_overrides[get_db] = lambda: in_memory_session
    with TestClient(app) as client:
        yield client
