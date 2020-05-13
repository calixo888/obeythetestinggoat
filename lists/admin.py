from django.contrib import admin
from lists import models

admin.site.register(models.ItemList)
admin.site.register(models.Item)
