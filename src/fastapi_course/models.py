from sqlalchemy.orm import DeclarativeBase
import sqlalchemy as sa
import datetime


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String, nullable=False, unique=True)
    password = sa.Column(sa.String, nullable=False)
    email = sa.Column(sa.String, nullable=False, unique=True)
    created_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now())
