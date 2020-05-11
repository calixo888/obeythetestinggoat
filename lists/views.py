from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):

    if request.method == "POST":

        # Create Item object
        models.Item.objects.create(text=request.POST["item-text"])


    # Get all items and send them into context for table population
    return render(request, "index.html", context={
        "items": models.Item.objects.all()
    })
