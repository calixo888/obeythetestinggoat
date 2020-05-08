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


    def test_save_a_post_request(self):
        """
        Make sure that the application can save a POST request to database
        """

        # Make POST request to index
        response = self.client.post("/", data={
            "item-text": "A new list item"
        })

        # Check if data is returned from POST response
        self.assertIn(
            "A new list item",
            response.content.decode()
        )

        # Make sure index.html template is rendered
        self.assertTemplateUsed(response, "index.html")


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
