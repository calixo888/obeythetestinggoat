from django.db import models

class List(models.Model):
    url_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):
    text = models.CharField(max_length=50)
    list = models.ForeignKey("List", on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.text
