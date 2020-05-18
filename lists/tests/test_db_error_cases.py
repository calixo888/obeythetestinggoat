from django.core.exceptions import ValidationError
from django.test import TestCase
from lists import views, models
from unittest import skip


class DBErrorCasesTest(TestCase):

    def test_create_empty_item_list_object(self):
        """
        Try to create an empty ItemList at the database level

        We are trying to induce an error by creating an empty ItemList
        """

        # Form incorrect (empty) ItemList object
        empty_list = models.ItemList(url_name="", name="")

        # Test if DB error is raised
        with self.assertRaises(ValidationError):
            empty_list.save()
            empty_list.full_clean()


    def test_create_empty_item_object(self):
        """
        Try to create an empty Item at the database level

        We are trying to induce an error by creating an empty Item
        """

        # Form valid list
        valid_list = models.ItemList.objects.create(url_name="sample-list", name="Sample List")

        # Form incorrect (empty) Item object
        empty_item = models.Item(item_list=valid_list, text="")

        # Test if DB error is raised
        with self.assertRaises(ValidationError):
            empty_item.save()
            empty_item.full_clean()


    
