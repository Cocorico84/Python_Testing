from server import app
import unittest


class BaseTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['LOGIN_DISABLED'] = False
        self.app = app.test_client()

    def login(self):
        return self.app.post('/showSummary', data={'email': "john@simplylift.co"}, follow_redirects=True)
