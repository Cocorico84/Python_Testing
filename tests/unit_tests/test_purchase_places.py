from tests.base import BaseTest


class PurchaseTest(BaseTest):
    def test_purchase_places_with_negative_number(self):

        response = self.app.post('/purchasePlaces', data={"club": "Simply Lift", "competition": "Spring Festival", "places": 30}, follow_redirects=True)
        assert response.status_code == 200
        assert b'You cannot buy more than your available places' in response.data
    
    def test_purchase_places(self):
        response = self.app.post('/purchasePlaces', data={"club": "Simply Lift", "competition": "Spring Festival", "places": 3}, follow_redirects=True)
        assert response.status_code == 200
        assert b'You cannot buy more than your available places' not in response.data

