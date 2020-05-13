from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import unittest
import time

class NewVisitorCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='../obeythetestinggoat/chromedriver')

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

    def wait_for_item_rendered_in_table(self, item_text):
        """
        Implicit wait function until item is rendered into table
        """

        start_time = time.time()
        while True:
            try:
                # Making sure table is populated with new to-do item
                to_do_item_table = self.browser.find_element_by_id("to-do-item-table")
                to_do_item_table_rows = to_do_item_table.find_elements_by_tag_name("tr")
                self.assertTrue(
                    any(row.text == item_text for row in to_do_item_table_rows)
                )

                return # End this function

            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > 10:
                    raise e

                time.sleep(0.5)


if __name__ == "__main__":
    unittest.main(warnings="ignore")
