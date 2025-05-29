from http import HTTPStatus


def test_read_root(client):
    # "Deve retornar OK e Hello World!"

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Afirmação)

    assert response.json() == {'message': 'Essa é a root do programa'}  # Assert de afirmação que confirma
    # se o resultado do request foi "Hello World"


def test_create_user(client):
    # Cria o usuario Pinoccio

    json = {'username': 'Pinoccio',
            'email': 'pinoccio@gmail.com',
            'password': 'senha_do_pinoccio'}

    response = client.post('/users/', json=json)

    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {'message': 'User created!'}


def test_create_user_CONFLICT_EMAIL(client, create_default_user):
    # Utiliza a fixture de criar usuario para cria-lo novamente.

    json = {'username': 'Vitor Ferreira',
            'email': 'default@email.com',
            'password': 'default_password'}

    response = client.post('/users/', json=json)

    assert response.status_code == HTTPStatus.CONFLICT

    assert response.json() == {'detail': 'Email or Username Already exists'}


def test_create_user_CONFLICT_USERNAME(client, create_default_user):
    # Utiliza a fixture de criar usuario para cria-lo novamente.

    json = {'username': 'default_name',
            'email': 'vitorferreira@email.com',
            'password': 'default_password'}

    response = client.post('/users/', json=json)

    assert response.status_code == HTTPStatus.CONFLICT

    assert response.json() == {'detail': 'Email or Username Already exists'}


def test_read_empty_user(client):
    # Testa se o json retornado é vazio, pois não foi adicionado nenhum usuario.

    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'users': []}


def test_read_user(client, create_default_user):
    # Recebe a fixture create_default_user para le-lo.

    response = client.get('/users/')
    must_be_json = {
        'email': 'default@email.com',
        'username': 'default_name',
        'id': 1
    }
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [must_be_json]}


def test_update_user(client, create_default_user):
    json = {'username': 'Zézinho',
            'email': 'emaildofihdoze@emaildofihdoze.com',
            'password': 'senha_do_zé123',
            'old_password': 'default_password'
            }

    response = client.put('/users/1', json=json)

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'message': 'user updated!'}


def test_update_user_NOTFOUND(client, create_default_user):
    json = {'username': 'Zézinho',
            'email': 'emaildofihdoze@emaildofihdoze.com',
            'password': 'senha_do_zé123',
            'old_password': 'default_password'
            }

    response = client.put('/users/3', json=json)

    assert response.status_code == HTTPStatus.NOT_FOUND

    assert response.json() == {'detail': 'User not found'}


def test_update_user_UNAUTHORIZED(client, create_default_user):
    json = {'username': 'Zézinho',
            'email': 'emaildofihdoze@emaildofihdoze.com',
            'password': 'senha_do_zé123',
            'old_password': 'wrong_password'
            }

    response = client.put('/users/1', json=json)

    assert response.status_code == HTTPStatus.UNAUTHORIZED

    assert response.json() == {'detail': 'Not the same password'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'message': 'User deleted'}
#
#
# def test_delete_exception_error_user_not_found(client):
#     response = client.delete('/users/2')
#
#     assert response.status_code == HTTPStatus.NOT_FOUND
#
#     assert response.json() == {'detail': 'User not found'}
