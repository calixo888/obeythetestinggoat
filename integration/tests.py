from django.test import TestCase
from lists import models


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
