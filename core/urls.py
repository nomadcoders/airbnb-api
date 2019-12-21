from django.urls import path
from . import views

app_name = "core"

urlpatterns = [path("list", views.list_rooms)]
