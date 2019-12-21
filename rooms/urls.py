from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [path("list/", views.list_rooms)]
