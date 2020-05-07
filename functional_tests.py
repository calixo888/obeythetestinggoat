from selenium import webdriver
import unittest

class NewVisitorCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='../obeythetestinggoat/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_start_list_and_retrieve_later(self):
        # Start the browser
        self.browser.get('http://localhost:8000')

        # Visitor checks the title to see the page
        self.assertIn("To-Do", self.browser.title)

        # Throw error and stop test
        self.fail("Finish the e2e test!")


if __name__ == "__main__":
    unittest.main(warnings="ignore")
