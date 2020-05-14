from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from . import models

def index(request):
    """
    Render the index page
    """

    return render(request, "index.html")

def new_list(request):
    """
    Create a new ItemList, then redirect to its unique URL
    """

    if request.method == "POST":
        item_list_name = request.POST.get("item-list-name")
        url_list_name = item_list_name.lower().replace(" ", "-")
        models.ItemList.objects.create(url_name=url_list_name, name=item_list_name)
        return HttpResponseRedirect(f"/lists/{url_list_name}/")

def add_item(request):
    """
    Create new item and link it to specific ItemList, then redirect back to ItemList page
    """

    if request.method == "POST":
        models.Item.objects.create(
            text = request.POST.get("item"),
            item_list = models.ItemList.objects.get(name=request.POST.get("item-list-name"))
        )

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def view_list(request, list_url_name):
    """
    View unique ItemList through unique dynamic URL extension
    """

    item_list = models.ItemList.objects.get(url_name=list_url_name)

    return render(request, "view-list.html", context={
        "item_list": item_list,
        "items": item_list.items.all()
    })
