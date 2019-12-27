from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [
    path("", views.rooms_view),
    path("<int:pk>/", views.SeeRoomView.as_view()),
]
