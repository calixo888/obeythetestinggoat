from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models

def index(request):
    return render(request, "index.html")

def new_list(request):
    item_list_name = request.POST["item-list-name"]
    url_list_name = item_list_name.lower().replace(" ", "-")
    models.ItemList.objects.create(url_name=url_list_name, name=item_list_name)
    return HttpResponseRedirect(f"/lists/{item_list_name}/")

def view_list(request):
    # Get all items and send them into context for table population
    return render(request, "view-list.html", context={
        "items": models.Item.objects.all()
    })
