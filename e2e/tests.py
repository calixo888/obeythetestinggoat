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

    def test_create_list_and_add_items(self):
        """
        Simulate creating a list and adding items to that list from the unique list view
        """
        # Start the browser
        self.browser.get(self.live_server_url)

        # ADD ITEM
        # Visitor is invited to create to-do item immediately
        item_list_input = self.browser.find_element_by_id("item-list-input")

        # Typing in a new to-do item
        item_list_input.send_keys("Sample List")

        # Creating new to-do item
        item_list_input.send_keys(Keys.ENTER)

        # Test that new list at unique URL is generated
        self.assertRegex(self.browser.current_url, "/lists/sample-list/")

        # ADD 3 ITEMS
        items = ["Item 1", "Item 2", "Item 3"]
        for item in items:
            # Grab input element
            to_do_item_input = self.browser.find_element_by_id("to-do-item-input")

            # Send keys to add item
            to_do_item_input.send_keys(item)
            to_do_item_input.send_keys(Keys.ENTER)

        # Test that all 3 items are in table
        to_do_items_table = self.browser.find_element_by_id("to-do-item-table")
        for item in items:
            self.assertTrue(
                any(row.text == item for row in to_do_items_table.find_elements_by_tag_name("tr"))
            )


if __name__ == "__main__":
    unittest.main(warnings="ignore")
