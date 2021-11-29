from flask import Flask
from flask_testing import LiveServerTestCase
from selenium import webdriver
import time
from flask import url_for
from flask_unittest import LiveTestCase

class LoginTest(LiveTestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 0
        return app
    
    def setUp(self):
        self.driver = webdriver.Chrome("tests/functional_tests/chromedriver")
        # self.driver.get("http://127.0.0.1:5000/")
        return super().setUp()
    
    # def tearDown(self):
    #     self.driver.quit()
    
    # def test_login(self):
    #     email = self.driver.find_element_by_name("email")
    #     email.send_keys('john@simplylift.co')
    #     signup = self.browser.find_element_by_type("submit")
    #     signup.click()

    def test_server_is_up_and_running(self):
        self.driver.get(self.server_url)
        time.sleep(30)
