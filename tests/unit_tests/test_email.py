import pytest
import server


@pytest.fixture
def client():
    return server.app.test_client()


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200


def test_login_with_unknown_email(client):
    response = client.post('/showSummary', data={"email": "unknow@email.com"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Your club is not registered!" in response.data


def test_login_with_known_email(client):
    response = client.post('/showSummary', data={"email": "john@simplylift.co"}, follow_redirects=True)
    assert response.status_code == 200
