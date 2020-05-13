from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from . import models

def index(request):
    return render(request, "index.html")

def new_list(request):
    item_list_name = request.POST["item-list-name"]
    url_list_name = item_list_name.lower().replace(" ", "-")
    models.ItemList.objects.create(url_name=url_list_name, name=item_list_name)
    return HttpResponseRedirect(f"/lists/{url_list_name}/")

def add_item(request):
    if request.method == "POST":
        models.Item.objects.create(
            text = request.POST.get("item"),
            item_list = models.ItemList.objects.get(name=request.POST.get("item-list-name"))
        )

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def view_list(request, list_url_name):
    # Get list from list_url_name
    item_list = models.ItemList.objects.get(url_name=list_url_name)

    # Get all items and send them into context for table population
    return render(request, "view-list.html", context={
        "item_list": item_list,
        "items": item_list.items.all()
    })
