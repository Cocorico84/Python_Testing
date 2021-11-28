import pytest
import server

@pytest.fixture
def client():
    return server.app.test_client()

@pytest.mark.django_db
def test_login_route(client):

    home = client.get('/')
    assert home.status_code == 200

    login = client.post('/showSummary', data={"email": "john@simplylift.co"}, follow_redirects=True)
    assert login.status_code == 200

    logout = client.get('/logout', follow_redirects=True)
    assert logout.status_code == 200