from http import HTTPStatus


def test_read_root(client):  # "Deve retornar OK e Hello World!"

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Afirmação)

    assert response.json() == {'message': 'Hello World!'}  # Assert de afirmação que confirma
    # se o resultado do request foi "Hello World"


def test_create_user(client):
    json = {'username': 'Zézão', 'password': 'senha_do_zé123', 'email': 'emaildozé@emaildoze.com'}

    response = client.post('/users/', json=json)

    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {'username': 'Zézão', 'email': 'emaildozé@emaildoze.com', 'id': 1}


def test_read_user(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'users': [
        {'username': 'Zézão', 'email': 'emaildozé@emaildoze.com', 'id': 1}
    ]}


def test_update_user(client):
    json = {'username': 'Zézinho', 'email': 'emaildofihdoze@emaildofihdoze.com', 'password': 'senha_do_zé123'}

    response = client.put('/users/1', json=json)

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'id': 1, 'username': 'Zézinho', 'email': 'emaildofihdoze@emaildofihdoze.com'}


def test_exception_error_user_not_found(client):
    json = {'username': 'Zézinho', 'email': 'emaildofihdoze@emaildofihdoze.com', 'password': 'senha_do_zé123'}

    response = client.put('/users/2', json=json)

    assert response.status_code == HTTPStatus.NOT_FOUND

    assert response.json() == {'detail': 'User not found'}


def test_update_exception_error_wrong_password(client):
    json = {'username': 'Zézinho', 'email': 'emaildofihdoze@emaildofihdoze.com', 'password': 'senha_errada123'}

    response = client.put('/users/1', json=json)

    assert response.status_code == HTTPStatus.UNAUTHORIZED

    assert response.json() == {'detail': 'Not the same password'}


def test_get_password_error_exception_error_user_not_found(client):
    response = client.get('/users/getpassword/2')

    assert response.status_code == HTTPStatus.NOT_FOUND

    assert response.json() == {'detail': 'User not found'}


def test_get_password(client):
    response = client.get('/users/getpassword/1')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'password': 'senha_do_zé123'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'message': 'User deleted'}


def test_delete_exception_error_user_not_found(client):
    response = client.delete('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND

    assert response.json() == {'detail': 'User not found'}
