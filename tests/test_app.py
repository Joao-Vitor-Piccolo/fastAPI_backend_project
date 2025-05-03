from http import HTTPStatus


def test_read_root(client):  # "Deve retornar OK e Hello World!"

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Afirmação)

    assert response.json() == {'message': 'Hello World!'}  # Assert de afirmação que confirma
    # se o resultado do request foi "Hello World"


def test_create_user(client):
    json = {'username': 'testusername', 'password': 'passwordtest12', 'email': 'emaildozé@emaildoze.com'}

    response = client.post('/users/', json=json)

    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {'username': 'testusername', 'email': 'emaildozé@emaildoze.com', 'id': 1}


def test_read_user(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'users': [
        {'username': 'testusername', 'email': 'emaildozé@emaildoze.com', 'id': 1}
    ]}

