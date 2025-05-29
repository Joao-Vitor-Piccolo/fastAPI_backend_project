import pytest
from fastapi_course.models import Base
from sqlalchemy.orm import Session
from src.fastapi_course.app import app
from fastapi.testclient import TestClient
from datetime import datetime
from sqlalchemy import create_engine, event
from fastapi_course.models import UserDB
from fastapi_course.database import get_session
from sqlalchemy.pool import StaticPool


@pytest.fixture()
def client(session):  # Usa a fixture de session que possui o SQLite em memoria
    def get_session_override():  # Nós criamos a função pois o Depends() pede extritamente uma function
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client
    app.dependency_overrides.clear()  # Serve para outros testes não acabarem usando o override acima sem querer


@pytest.fixture()
def session():
    engine = create_engine('sqlite:///:memory:',
                           connect_args={'check_same_thread': False},  # Remove a restrição de multithread do Sqlite
                           poolclass=StaticPool
                           )

    Base.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    Base.metadata.drop_all(engine)


@pytest.fixture()
def create_default_user(session):
    @event.listens_for(UserDB, 'before_insert')
    def listen_time(mapper, connection, target):
        if hasattr(target, 'created_at'):
            target.created_at = datetime(day=12, month=12, year=2012)
        if hasattr(target, 'updated_at'):
            target.updated_at = datetime(day=12, month=12, year=2012)

    user = UserDB(username='default_name', email='default@email.com', password='default_password')
    session.add(user)
    session.commit()
    session.refresh(user)
