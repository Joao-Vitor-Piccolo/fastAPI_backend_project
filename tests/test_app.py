from fastapi.testclient import TestClient
from src.fastapi_course.app import app  # Importamos desta forma pois o import é realizado na raiz do projeto.
from http import HTTPStatus


## client = TestClient(app)  # Colocamos aqui o objeto app, no caso o app.py que criamos na main.


# Ou seja, o objeto que queremos testar


def test_read_root():  # "Deve retornar OK e Hello World!"
    client = TestClient(app)  # Arrange (Organização do teste)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Afirmação)

    assert response.json() == {'message': 'Hello World!'}  # Assert de afirmação que confirma
    # se o resultado do request foi "Hello World"


def test_create_user():
    client = TestClient(app)  # Arrange (Organização do teste)

    headers = {
        "username": "João",
        "email": "joao@example.com",
        "password": "renatinho123"
    }

    response = client.post('/users/', json=headers)  # Act (ação)

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'message': 'User Created'}


def test_read_user():
    pass
