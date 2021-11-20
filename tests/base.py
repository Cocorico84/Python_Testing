from server import app
import unittest


class BaseTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['LOGIN_DISABLED'] = False
        self.app = app.test_client()
