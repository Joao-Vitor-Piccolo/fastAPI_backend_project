from fastapi import FastAPI, HTTPException, Depends
from fastapi_course.schemas import *
from http import HTTPStatus
from fastapi_course.database import get_session
from sqlalchemy import select, delete
from fastapi_course.models import UserDB

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Essa é a root do programa'}


# Criamos uma função user que recebe como parametro a classe User, que criamos em Schemas, mudando
# o decorators para um metodo POST

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=Message)
def create_user(user: User_Schema, session=Depends(get_session)):
    db_user = session.scalar(select(UserDB).where((UserDB.username == user.username) | (UserDB.email == user.email)))
    if db_user:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail='Email or Username Already exists')
    else:
        db_user = UserDB(username=user.username, email=user.email, password=user.password)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return {'message': 'User created!'}


@app.get('/users/', response_model=UserList, status_code=HTTPStatus.OK)
# query_limit: int = 10 Cria um query
# parameter personalizavel que tem como padrão 10 resultados

def read_users(query_limit: int = 1, session=Depends(get_session)):
    db_user = session.scalars(select(UserDB).limit(limit=query_limit))
    return {'users': db_user}


@app.put('/users/{user_id}', response_model=Message, status_code=HTTPStatus.OK)
def update_user(user_id: int, user: UserUpdate, session=Depends(get_session)):
    db_user = session.scalar(select(UserDB).where(user_id == UserDB.id))
    if not db_user:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')

    if db_user.password != user.old_password:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail='Not the same password')

    db_user.password = user.password
    db_user.username = user.username
    db_user.email = user.email
    session.commit()
    session.refresh(db_user)
    return {'message': 'user updated!'}


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int, user: User_Schema, session=Depends(get_session)):
    db_user = session.scalar(select(UserDB).where(user_id == UserDB.id))
    if not db_user:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')

    if not (db_user.password == user.password and db_user.username == user.username and db_user.email == user.email):
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail='Not the same email, username or password')

    session.execute(delete(UserDB).where(UserDB.id == user_id))
    session.commit()
    return {'message': 'User deleted!'}
