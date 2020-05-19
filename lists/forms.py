from django import forms
from lists import models

# ERROR MESSAGE VARS
EMPTY_ITEM_ERROR = "You must enter in text for the item."

class ItemForm(forms.models.ModelForm):
    """
    Form for Item object
    """

    class Meta:
        model = models.Item
        fields = ('text',)
        widgets = {
            "text": forms.fields.TextInput(attrs={
                "placeholder": "Enter a to-do item",
                "class": "form-control input-lg"
            })
        }

        error_messages = {
            "text": {
                "required": EMPTY_ITEM_ERROR
            }
        }
