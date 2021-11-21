
import pytest
import server


@pytest.fixture
def client():
    return server.app.test_client()

@pytest.fixture
def club_data(monkeypatch):
    monkeypatch.setattr('server.clubs', [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13"
        }
    ])

@pytest.fixture
def competition_data(monkeypatch):
    monkeypatch.setattr('server.competitions', [
        {
            "name": "Spring Festival",
            "date": "2022-03-27 10:00:00",
            "numberOfPlaces": "25"
        }
    ])

    

def test_update_clubs_and_competitions(client, competition_data, club_data):
    response = client.post('/purchasePlaces', data={
                                "club": "Simply Lift", "competition": "Spring Festival", "places": 3}, follow_redirects=True)
    assert response.status_code == 200
    assert server.clubs[0]['points'] == 10
    assert server.competitions[0]['numberOfPlaces'] == 22


def test_update_not_enough_points(client, competition_data, club_data):
    client.post('/purchasePlaces', data={
                                "club": "Simply Lift", "competition": "Spring Festival", "places": 12}, follow_redirects=True)
    response = client.post('/purchasePlaces', data={
                                "club": "Simply Lift", "competition": "Spring Festival", "places": 12}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Not enough points to buy places!" in response.data
