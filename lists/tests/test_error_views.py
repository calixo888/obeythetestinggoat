from django.test import TestCase
from lists import views, models

class ErrorTest(TestCase):

    def test_404(self):
        """
        Test going to a null URL and expect a custom 404 page
        """

        # Make GET request to null URL
        response = self.client.get("/this-url-doesnt-exist/")

        # Test the status and template of response
        self.assertEquals(response.status_code, 404)
        self.assertTemplateUsed("404.html")

        # Test the content of the custom 404 template
        self.assertIn("Custom 404 page", response.content.decode())
