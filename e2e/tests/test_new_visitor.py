from .base import E2ETest
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorCase(E2ETest):

    def test_create_list_and_add_items(self):
        """
        Simulate creating a list and adding items to that list from the unique list view
        """
        # Start the browser
        self.browser.get(self.live_server_url)

        # Go the Create List
        create_list_link = self.browser.find_element_by_id("nav-item-create-list")
        create_list_link.click()

        time.sleep(.5)

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
            # Wait for page to render
            time.sleep(.5)

            # Grab input element
            to_do_item_input = self.browser.find_element_by_id("to-do-item-input")

            # Send keys to add item
            to_do_item_input.send_keys(item)
            to_do_item_input.send_keys(Keys.ENTER)

        # Test that all 3 items are in table
        to_do_items_table = self.browser.find_element_by_id("to-do-item-list")
        for item in items:
            self.assertTrue(
                any(list_item.text == item for list_item in to_do_items_table.find_elements_by_tag_name("li"))
            )
