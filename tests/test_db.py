from fastapi_course.models import User
from sqlalchemy import select, event
from datetime import datetime


def test_create_user(session):
    time = datetime(day=12, month=12, year=2012)

    @event.listens_for(User, 'before_insert')
    def listen_time(mapper, connection, target):
        if hasattr(target, 'created_at'):
            target.created_at = time
        if hasattr(target, 'updated_at'):
            target.updated_at = time

    user = User(username='janjo', email='janjo@janjomail.com', password='senhaboa123')
    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.username == 'janjo')).__dict__

    result.pop('_sa_instance_state')

    assert result == {'id': 1,
                      'username': 'janjo',
                      'email': 'janjo@janjomail.com',
                      'password': 'senhaboa123',
                      'created_at': time,
                      'updated_at': time
                      }
    event.remove(User, 'before_insert', listen_time)


def test_update_user(session, create_default_user):
    user = session.scalar(select(User))
    user.username = 'laercio'
    session.commit()
    assert user.created_at != user.updated_at
