from fastapi.testclient import TestClient
from src.fastapi_course.app import app  # Importamos desta forma pois o import é realizado na raiz do projeto.
from http import HTTPStatus


client = TestClient(app)  # Colocamos aqui o objeto app que criamos no app.py


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (Organização do teste)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Afirmação)

    assert response.json() == {'message': 'Hello World!'}
