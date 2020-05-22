from django.conf.urls import url
from lists import views

urlpatterns = [
    url("^$", views.index, name="index"),
    url("^create-list/$", views.create_list, name="create_list"),
    url("^lists/new/$", views.new_list, name="new_list"),
    url("^lists/add-item/$", views.add_item, name="add_item"),
    url("^lists/(.+)/$", views.view_list, name="view_list"),
]
