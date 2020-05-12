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
        to_do_item_input = self.browser.find_element_by_id("to-do-item-input")

        # Typing in a new to-do item
        to_do_item_input.send_keys("Buy some milk")

        # Creating new to-do item
        to_do_item_input.send_keys(Keys.ENTER)

        # Implicit wait and check for item to be rendered in table
        self.wait_for_item_rendered_in_table("Buy some milk")

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

    def test_user_can_start_list_at_unique_url(self):
        """
        Be able to create a unique URL for a new list
        """

        # Get index page
        self.browser.get(self.live_server_url)

        # Create a new list item
        to_do_item_input = self.browser.find_element_by_id("to-do-item-input")
        to_do_item_input.send_keys("Eat some cats")
        to_do_item_input.send_keys(Keys.ENTER)

        # Check for new item in table
        self.wait_for_item_rendered_in_table("Eat some cats")

        # Check for newly generated URL for list
        generated_list_url = self.browser.current_url
        self.assertRegex(generated_list_url, "/lists/.+") # Check the regex


if __name__ == "__main__":
    unittest.main(warnings="ignore")
