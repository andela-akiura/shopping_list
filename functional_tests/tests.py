from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.
class TestUserRegister(LiveServerTestCase):
    fixtures = ['admin_user.json']

    def setUp(self):
        self.browser = webdriver.Chrome(
            '/Users/heavy_machinery/webdrivers/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_user_register_and_login(self):
        self.browser.get(self.live_server_url + '/register/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Sign up', body.text)

        # create an account
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('kiura')
        email_field = self.browser.find_element_by_name('email')
        email_field.send_keys('kiuraalex@gmail.com')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('password')
        password_field.send_keys(Keys.RETURN)
        body = self.browser.find_element_by_tag_name('body')

        # check whether user is prompted to login (successful registration)
        self.assertIn('Sign in', body.text)

        # login
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('kiura')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('password')
        password_field.send_keys(Keys.RETURN)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Hello kiura', body.text)
