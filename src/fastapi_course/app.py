from fastapi import FastAPI
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

    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_with_id)
    return user_with_id
