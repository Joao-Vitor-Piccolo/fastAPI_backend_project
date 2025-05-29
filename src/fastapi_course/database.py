from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from fastapi_course.settings import Settings

engine = create_engine(Settings().DATABASE_URL)

session = Session(engine)


def get_session():
    with Session(engine) as session:
        yield session
