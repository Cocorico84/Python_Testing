import pytest
import server
from tests.base import BaseTest


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

class PurchaseTest(BaseTest):
    def test_purchase_place(self):
        self.app.get('/')
        self.app.post('/showSummary', data={"email": "john@simplylift.co"}, follow_redirects=True)

        response = self.app.post('/purchasePlaces', data={"club": "Simply Lift", "competition": "Spring Festival", "places": 3}, follow_redirects=True)
        assert response.status_code == 200
        assert server.clubs[0]['points'] == 4
        assert server.competitions[0]['numberOfPlaces'] == 22
        assert b'You cannot buy more than your available places' not in response.data
        assert b'You cannot buy more than 12 places!' not in response.data
        assert b"Something went wrong-please try again" not in response.data
        assert b"Not enough points to buy places!" not in response.data
