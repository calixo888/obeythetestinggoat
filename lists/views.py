from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from . import models, forms

def index(request):
    """
    Render the index page
    """

    return render(request, "index.html")


def create_list(request):
    """
    Render the Create List page
    """

    return render(request, "create-list.html")


def new_list(request):
    """
    Create a new ItemList, then redirect to its unique URL
    If provided ItemList name is empty, return HttpResponse error
    """

    if request.method == "POST":
        item_list_name = request.POST.get("item-list-name")

        # Check if item_list_name is empty
        if item_list_name:
            url_list_name = item_list_name.lower().replace(" ", "-")
            models.ItemList.objects.create(url_name=url_list_name, name=item_list_name)
            return HttpResponseRedirect(f"/lists/{url_list_name}/")

        else:
            return HttpResponse("No list name provided.", status=500)


def add_item(request):
    """
    Create new item and link it to specific ItemList, then redirect back to ItemList page
    """

    if request.method == "POST":
        item_list_name = request.POST.get("item-list-name")
        item_list = models.ItemList.objects.get(name=item_list_name)

        item_form = forms.ItemForm(request.POST)

        # Check if item_text is empty
        if item_form.is_valid():
            models.Item.objects.create(
                text=item_form.cleaned_data["text"],
                item_list=item_list
            )

        else:
            return HttpResponseRedirect(f"/lists/{item_list.url_name}")

    return HttpResponseRedirect(f"/lists/{item_list.url_name}")

def view_list(request, list_url_name):
    """
    View unique ItemList through unique dynamic URL extension
    """

    item_list = models.ItemList.objects.get(url_name=list_url_name)
    item_form = forms.ItemForm()

    return render(request, "view-list.html", context={
        "item_list": item_list,
        "items": item_list.items.all(),
        "item_form": item_form
    })
