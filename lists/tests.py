from django.test import TestCase
from django.urls import resolve
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

        # Make a POST request to server to create new list
        response = self.client.post("/lists/new/", data={
            "item-list-name": "Sample List"
        })

        # Test the amount of objects in DB is 1
        self.assertEqual(models.ItemList.objects.count(), 1)

        # Test if the (first) item is the item we submitted
        first_item_list = models.ItemList.objects.first()
        self.assertEqual(first_item_list.name, "Sample List")

    def test_new_list_table_is_empty(self):
        """
        Make sure that the table of the new list is empty on creation
        """

        # Create a new list
        item_list = models.ItemList(
            url_name="sample-list",
            name="Sample List"
        )
        item_list.save()

        # Test how many items linked to a brand new ItemList -> should be 0
        self.assertEquals(item_list.items.count(), 0)
