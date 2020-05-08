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

        response = self.client.get("/")
        html = response.content.decode('utf8')

        self.assertTemplateUsed(response, "index.html")
