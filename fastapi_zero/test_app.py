from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app

clientest = TestClient(app)


def test_root_dev_retornar_Hello_World():
    clientest = TestClient(app)

    """ Esse teste tem 3 etapas (Arrange, Act, Assert) 

    Arrange: Preparar o cenário do teste
    Act: Executar a ação que queremos testar
    Assert: Verificar se o resultado é o esperado

    """
    # Arrange: Preparar o cenário do teste
    clientest.get('/')
    # Act: Executar a ação que queremos testar
    response = clientest.get('/')
    # assert: Verificar se o resultado é o esperado
    assert response.json() == {'message': 'Hello World!'}
    assert response.status_code == HTTPStatus.OK

