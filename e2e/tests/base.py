from django.test import LiveServerTestCase
from selenium import webdriver
import unittest
import os

class E2ETest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='../obeythetestinggoat/chromedriver')

        staging_server = os.environ.get("STAGING_SERVER")
        if staging_server:
            self.live_server_url = 'http://' + staging_server

        self.browser.set_window_size(1500, 1000)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main(warnings="ignore")
