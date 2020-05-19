from django.test import TestCase
from lists import forms

class FormsTest(TestCase):

    def test_item_form_has_text_input(self):
        """
        Test that ItemForm renders a text input
        """

        # Create ItemForm
        item_form = forms.ItemForm()

        # Test content of HTML-rendered ItemForm
        self.assertIn('placeholder="Enter a to-do item"', item_form.as_p())
        self.assertIn('class="form-control input-lg"', item_form.as_p())


    def test_item_form_validation_for_blank_input(self):
        """
        Test ItemForm validation by submitting with blank inputs
        """

        item_form = forms.ItemForm(data={'text': ''})

        # Expect a ValueError
        with self.assertRaises(ValueError):
            item_form.save()

        # Test the specific error message
        self.assertEqual(
            item_form.errors["text"],
            [forms.EMPTY_ITEM_ERROR]
        )
