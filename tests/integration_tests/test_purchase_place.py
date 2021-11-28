from tests.base import BaseTest


class PurchaseTest(BaseTest):
    def test_purchase_place(self):
        self.app.get('/')
        self.app.post('/showSummary', data={"email": "john@simplylift.co"}, follow_redirects=True)

        response = self.app.post('/purchasePlaces', data={"club": "Simply Lift", "competition": "Spring Festival", "places": 30}, follow_redirects=True)
        assert response.status_code == 200
