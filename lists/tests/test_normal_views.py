from django.test import TestCase
from lists import views, models, forms

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


    def test_view_list_uses_item_form(self):
        """
        Make sure that '/lists/:id/' uses the ItemForm custom form
        """

        # Create a sample list
        models.ItemList.objects.create(url_name="sample-list", name="Sample List")

        # GET request to '/lists/sample-list/'
        response = self.client.get("/lists/sample-list/")

        # Check if ItemForm is used inside template
        self.assertIsInstance(response.context["item_form"], forms.ItemForm)
