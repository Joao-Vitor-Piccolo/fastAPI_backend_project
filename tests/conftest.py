import pytest
from fastapi_course.models import Base
from sqlalchemy.orm import Session
from src.fastapi_course.app import app
from fastapi.testclient import TestClient
from contextlib import contextmanager
from datetime import datetime
from sqlalchemy import create_engine, event
from fastapi_course.models import User


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


@pytest.fixture()
def create_default_user(session):
    @event.listens_for(User, 'before_insert')
    def listen_time(mapper, connection, target):
        if hasattr(target, 'created_at'):
            target.created_at = datetime(day=12, month=12, year=2012)
        if hasattr(target, 'updated_at'):
            target.updated_at = datetime(day=12, month=12, year=2012)

    user = User(username='jorge', email='janjo@janjomail.com', password='senhaboa123')
    session.add(user)
    session.commit()
