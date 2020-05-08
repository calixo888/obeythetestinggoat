from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='../obeythetestinggoat/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_start_list_and_retrieve_later(self):
        # Start the browser
        self.browser.get('http://localhost:8000')

        # Testing title content
        self.assertIn(
            "To-Do",
            self.browser.title
        )

        # Visitor is invited to create to-do item immediately
        to_do_item_input = self.browser.find_element_by_id("#to-do-item-input")

        # Testing input placeholder text
        self.assertEqual(
            to_do_item_input.get_attribute("placeholder"),
            "Enter a to-do item"
        )

        # Typing in a new to-do item
        to_do_item_input.send_keys("Buy some milk")

        # Creating new to-do item
        to_do_item_input.send_keys(Keys.ENTER)

        time.sleep(1)

        # Making sure table is populated with new to-do item
        to_do_item_table = self.browser.find_element_by_id("to-do-item-table")
        to_do_item_table_rows = to_do_item_table.find_elements_by_tag_name("tr")
        self.assertTrue(
            any(row.text == "Buy some milk" for row in to_do_item_table_rows)
        )


if __name__ == "__main__":
    unittest.main(warnings="ignore")
