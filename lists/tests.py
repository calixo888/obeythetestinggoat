from django.test import TestCase
from django.urls import resolve
from lists import views, models

class HomePageTest(TestCase):

    def test_root_url_is_index(self):
        """
        Check if the index page is accessed through the root URL
        """

        root_page = resolve("/")
        self.assertEqual(root_page.func, views.index)


    def test_index_has_correct_html(self):
        """
        Make sure that the index page renders the index.html template
        """

        # Make GET request to index
        response = self.client.get("/")

        # Grab HTML from GET response
        html = response.content.decode('utf8')

        # Make sure that the template rendered in index.html
        self.assertTemplateUsed(response, "index.html")


    def test_all_items_are_rendered_in_table(self):
        """
        Make sure that all items in database are being rendered in the table
        """

        # Create 2 items
        models.Item.objects.create(text="Item 1")
        models.Item.objects.create(text="Item 2")

        # Make GET request to index page
        response = self.client.get("/")

        # Check if the items 1 and 2 are in response content
        self.assertIn("Item 1", response.content.decode())
        self.assertIn("Item 2", response.content.decode())


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        """
        Test creating and saving the Item model into the database
        """

        # Create 2 Item objects
        models.Item.objects.create(text="First List Item")
        models.Item.objects.create(text="Second List Item")

        # Get all Item objects from database
        saved_items = models.Item.objects.all()

        # Test how many items are saved in database
        self.assertEqual(saved_items.count(), 2)

        # Grab each Item object
        first_item_object = saved_items[0]
        second_item_object = saved_items[1]

        # Test the 'text' field of each item
        self.assertEqual(first_item_object.text, "First List Item")
        self.assertEqual(second_item_object.text, "Second List Item")


    def test_save_a_post_request(self):
        """
        Test that making a POST request will save Item object in database
        """

        test_item_text = "New list item"

        # Make a POST request to server
        response = self.client.post("/", data={
            "item-text": test_item_text
        })

        # Test the amount of objects in DB is 1
        self.assertEqual(models.Item.objects.count(), 1)

        # Test if the (first) item is the item we submitted
        first_item = models.Item.objects.first()
        self.assertEqual(first_item.text, test_item_text)


    def test_redirects_to_index_after_post(self):
        """
        Test that we redirect to index page after POST request
        """

        test_item_text = "New list item"

        # Make a POST request to server
        response = self.client.post("/", data={
            "item-text": test_item_text
        })

        # Test the status code and URL location from HTML content
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("index.html")
