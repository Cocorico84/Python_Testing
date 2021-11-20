from tests.base import BaseTest


class MaxLimitPlacesTest(BaseTest):
    def test_purchase_less_than_twelve_places(self):
        response = self.app.post('/purchasePlaces', data={"club": "Simply Lift", "competition": "Spring Festival", "places": 3}, follow_redirects=True)
        assert response.status_code == 200
        assert b'You cannot buy more than 12 places!' not in response.data

    def test_purchase_more_than_twelve_places(self):
        response = self.app.post('/purchasePlaces', data={"club": "Simply Lift", "competition": "Spring Festival", "places": 13}, follow_redirects=True)
        assert response.status_code == 200
        assert b'You cannot buy more than 12 places!' in response.data
