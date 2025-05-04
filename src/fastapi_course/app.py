from fastapi import FastAPI, HTTPException
from fastapi_course.schemas import *
from http import HTTPStatus

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World!'}


# Criamos uma função user que recebe como parametro a classe User, que criamos em Schemas, mudando
# o decorators para um metodo POST
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: User):
    c_user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(c_user_with_id)
    return c_user_with_id


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: User):
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
