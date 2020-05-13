from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import unittest
import time

class NewVisitorCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='../obeythetestinggoat/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_start_list_and_retrieve_later(self):
        # Start the browser
        self.browser.get(self.live_server_url)

        # Visitor is invited to create to-do item immediately
        item_list_input = self.browser.find_element_by_id("item-list-input")

        # Typing in a new to-do item
        item_list_input.send_keys("Sample List")

        # Creating new to-do item
        item_list_input.send_keys(Keys.ENTER)

        # Check that new list at unique URL is generated
        self.assertRegex(self.browser.current_url, "/lists/sample-list/")


if __name__ == "__main__":
    unittest.main(warnings="ignore")
