from django.db import models

class ItemList(models.Model):
    url_name = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    text = models.CharField(max_length=50, unique=True)
    item_list = models.ForeignKey(ItemList, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return self.text
