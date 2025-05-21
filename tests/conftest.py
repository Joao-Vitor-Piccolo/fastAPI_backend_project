import pytest
from sqlalchemy import create_engine, select
from fastapi_course.models import User, Base
from sqlalchemy.orm import Session
from src.fastapi_course.app import app
from fastapi.testclient import TestClient


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    Base.metadata.drop_all(engine)
