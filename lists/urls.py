from django.conf.urls import url
from lists import views

urlpatterns = [
    url("^$", views.index, name="index"),
]
