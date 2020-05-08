from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == "POST":
        return render(request, "index.html", context={
            "new_item_text": request.POST["item-text"]
        })

    return render(request, "index.html")
