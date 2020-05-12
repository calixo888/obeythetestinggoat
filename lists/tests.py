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


class NewListTest(TestCase):

    def test_save_a_POST_request(self):
        """
        Test that making a POST request will save Item object in database
        """

        # Make a POST request to server
        response = self.client.post("/", data={
            "item-text": "New list item"
        })

        # Test the amount of objects in DB is 1
        self.assertEqual(models.Item.objects.count(), 1)

        # Test if the (first) item is the item we submitted
        first_item = models.Item.objects.first()
        self.assertEqual(first_item.text, "New list item")

    def test_redirects_after_POST(self):
        """
        Test that we redirect to view-list page after POST request
        """

        # Make a POST request to server
        response = self.client.post("/", data={
            "item-text": "New list item"
        })

        # Test the status code and URL location from HTML content
        self.assertRedirects(response, "/lists/new-list/") # Detect URL redirect


class ListViewTest(TestCase):

    def test_list_displays_all_items(self):
        """
        Make sure that list page displays all items
        """

        # Create 2 new items
        models.Item.objects.create(text="Item 1")
        models.Item.objects.create(text="Item 2")

        # Get new-list page
        response = self.client.get("/lists/new-list/")

        # Check if page content includes 2 newly-created items
        self.assertContains(response, "Item 1")
        self.assertContains(response, "Item 2")
