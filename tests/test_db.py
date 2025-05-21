from fastapi_course.models import User
from sqlalchemy import select


def test_create_user(session):
    user = User(username='janjo', email='janjo@janjomail.com', password='senhaboa123')
    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.username == 'janjo'))

    assert result.username == 'janjo'
