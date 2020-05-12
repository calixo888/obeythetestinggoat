from django.conf.urls import url
from lists import views

urlpatterns = [
    url("^$", views.index, name="index"),
    url("^lists/new/$", views.new_list, name="new_list"),
    url("^lists/new-list/$", views.view_list, name="view_list"),
]
