from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models

def index(request):
    return render(request, "index.html")

def new_list(request):
    models.Item.objects.create(text=request.POST["item-text"])
    return HttpResponseRedirect("/lists/new-list/")

def view_list(request):
    # Get all items and send them into context for table population
    return render(request, "view-list.html", context={
        "items": models.Item.objects.all()
    })
