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


    def test_create_empty_list(self):
        """
        Try to create an empty list -> expect an HttpResponse error
        """

        # Make POST request to index with empty list-item data
        response = self.client.post("/lists/new/", data={
            "item-list-name": ""
        })

        # Test if HttpResponse error is received
        self.assertEquals(response.status_code, 500)
        self.assertIn("No list name provided.", response.content.decode())


    def test_create_empty_list_item(self):
        """
        Try to create a new item in a list with no text -> expect an HttpResponse error
        """

        # Make POST request to create list item with no text
        response = self.client.post("/lists/add-item/", data={
            "item": ""
        })

        # Test the status code and HttpResponse content 
        self.assertEquals(response.status_code, 500)
        self.assertIn("No list item text provided.", response.content.decode())
