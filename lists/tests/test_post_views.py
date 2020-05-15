from django.test import TestCase
from lists import views, models

class POSTViewTest(TestCase):

    def test_new_list(self):
        """
        Test new list creation when POST request made to '/lists/new/'
        """
        # Make POST request to '/lists/new/'
        response = self.client.post("/lists/new/", data={
            "item-list-name": "Sample List"
        })

        # Test amount of ItemLists created
        self.assertEquals(models.ItemList.objects.count(), 1)

        # Test fields of ItemList
        sample_list = models.ItemList.objects.get(name="Sample List")
        self.assertEquals(sample_list.name, "Sample List")
        self.assertEquals(sample_list.url_name, "sample-list")

    def test_add_item(self):
        """
        Test new item creation when POST request made to '/lists/add-item/'
        """
        # Create sample list
        models.ItemList.objects.create(
            url_name="sample-list",
            name="Sample List"
        )

        # Make POST request to '/lists/add-item/'
        response = self.client.post("/lists/add-item/", data={
            "item": "Sample List Item",
            "item-list-name": "Sample List"
        })

        # Test amount of Items created
        self.assertEquals(models.Item.objects.count(), 1)

        # Test content of new Item
        new_item = models.Item.objects.get(text="Sample List Item")
        self.assertEquals(new_item.text, "Sample List Item")
        self.assertEquals(new_item.item_list.name, "Sample List")
