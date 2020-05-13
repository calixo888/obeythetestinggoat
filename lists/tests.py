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

    def test_save_item(self):
        """
        Test saving an item to a test list
        """

        # Create a sample list
        item_list = models.ItemList(
            url_name="sample-list",
            name="Sample List"
        )
        item_list.save()

        # Create 2 items in sample list
        models.Item.objects.create(text="Item 1", item_list=item_list)
        models.Item.objects.create(text="Item 2", item_list=item_list)

        # Test objects inside DB
        self.assertEqual(models.Item.objects.count(), 2)
        self.assertEqual(models.Item.objects.all()[0].text, "Item 1")
        self.assertEqual(models.Item.objects.all()[1].text, "Item 2")


class NewListTest(TestCase):

    def test_create_item_list(self):
        """
        Test that making a POST request will save Item object in database
        """

        # Make a POST request to server
        response = self.client.post("/lists/new/", data={
            "item-list-name": "Sample List"
        })

        # Test the amount of objects in DB is 1
        self.assertEqual(models.ItemList.objects.count(), 1)

        # Test if the (first) item is the item we submitted
        first_item_list = models.ItemList.objects.first()
        self.assertEqual(first_item_list.name, "Sample List")

    def test_redirects_after_item_list_creation(self):
        """
        Test that we redirect to view-list page after POST request
        """

        # Make a POST request to server
        response = self.client.post("/lists/new/", data={
            "item-list-name": "Sample List"
        })

        # Test the status code and URL location from HTML content
        self.assertRedirects(response, "/lists/sample-list/") # Detect URL redirect


class ListViewTest(TestCase):
    def test_list_displays_all_items(self):
        """
        Make sure that list page displays all items
        """

        # Create a sample list
        item_list = models.ItemList(
            url_name="sample-list",
            name="Sample List"
        )
        item_list.save()

        # Create 2 items in sample list
        models.Item.objects.create(text="Item 1", item_list=item_list)
        models.Item.objects.create(text="Item 2", item_list=item_list)
    
        # Get new-list page
        response = self.client.get("/lists/sample-list/")

        # Check if page content includes 2 newly-created items
        self.assertContains(response, "Item 1")
        self.assertContains(response, "Item 2")
