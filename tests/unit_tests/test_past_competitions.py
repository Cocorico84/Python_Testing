from werkzeug.utils import redirect
from tests.base import BaseTest


class PastCompetitionsTest(BaseTest):
    def test_get_current_competitions(self):
        response = self.app.get('/book/Spring Festival/Simply Lift', follow_redirects=True)
        assert response.status_code == 200
        assert b"Something went wrong-please try again" not in response.data


    def test_get_past_competitions(self):
        response = self.app.get('/book/Fall Classic/Simply Lift', follow_redirects=True)
        assert response.status_code == 200
        assert b"Something went wrong-please try again" in response.data
