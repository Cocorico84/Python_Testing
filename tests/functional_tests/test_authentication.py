from flask import Flask
from flask_unittest import LiveTestCase
from selenium import webdriver


class LoginTest(LiveTestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app
    
    def setUp(self):
        self.driver = webdriver.Chrome("tests/functional_tests/chromedriver")
        self.driver.get("http://127.0.0.1:5000/")
        return super().setUp()
    
    def tearDown(self):
        self.driver.quit()
    
    def test_login(self):
        email = self.driver.find_element(by="name", value="email")
        email.send_keys('john@simplylift.co')
        signup = self.driver.find_element(by="tag name", value="button")
        signup.click()
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:5000/showSummary")
    
    def test_purchase_places(self):
        email = self.driver.find_element(by="name", value="email")
        email.send_keys('john@simplylift.co')
        signup = self.driver.find_element(by="tag name", value="button")
        signup.click()
        book_place = self.driver.find_element(by="xpath", value='//ul//a')
        book_place.click()
        book = self.driver.find_element(by="name", value='places')
        book.send_keys('3')
        button = self.driver.find_element(by="tag name", value="button")
        button.click()
        self.assertIn("Great-booking complete!", self.driver.page_source)
    
    def test_logout(self):
        email = self.driver.find_element(by="name", value="email")
        email.send_keys('john@simplylift.co')
        signup = self.driver.find_element(by="tag name", value="button")
        signup.click()
        logout = self.driver.find_element(by="tag name", value="a")
        logout.click()
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:5000/")
