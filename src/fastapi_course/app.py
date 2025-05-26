from fastapi import FastAPI, HTTPException, Depends
from fastapi_course.schemas import *
from http import HTTPStatus
from sqlalchemy.orm import Session
from fastapi_course.database import get_session
from sqlalchemy import select
from fastapi_course.models import UserDB

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Essa é a root do programa'}


# Criamos uma função user que recebe como parametro a classe User, que criamos em Schemas, mudando
# o decorators para um metodo POST

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=Message)
def create_user(user: User_Schema, session: Session = Depends(get_session)):
    db_user = session.scalar(select(UserDB).where((UserDB.username == user.username) | (UserDB.email == user.email)))
    if db_user:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail='Email or Username Already exists')
    else:
        db_user = UserDB(username=user.username, email=user.email, password=user.password)
        session.add(db_user)
        session.commit()
        return {'message': 'User created!'}


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: User_Schema):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(status_code=404, detail='User not found')

    if database[user_id - 1].password != user.password:
        raise HTTPException(status_code=401, detail='Not the same password')

    r_user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = r_user_with_id
    print(database)
    print(r_user_with_id)
    return r_user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(status_code=404, detail='User not found')

    del database[user_id - 1]
    return {'message': 'User deleted'}


@app.get('/users/getpassword/{user_id}', response_model=MessagePassword)
def get_password(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(status_code=404, detail='User not found')

    return {'password': database[user_id - 1].password}
