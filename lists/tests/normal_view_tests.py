from django.test import TestCase
from lists import views, models

class NormalViewTest(TestCase):

    def test_index_render(self):
        """
        Make sure URL '/' renders index.html
        """
        # GET request to '/'
        response = self.client.get("/")

        # Test template being rendered
        self.assertTemplateUsed(response, "index.html")

    def test_view_list_render(self):
        """
        Make sure URL '/lists/:id/' renders index.html
        """
        # Create sample list
        models.ItemList.objects.create(
            url_name="sample-list",
            name="Sample List"
        )

        # GET request to '/'
        response = self.client.get("/lists/sample-list/")

        # Test template being rendered
        self.assertTemplateUsed(response, "view-list.html")
