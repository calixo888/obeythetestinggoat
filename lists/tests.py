from django.test import TestCase
from django.urls import resolve
from lists import views

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
