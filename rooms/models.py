from django.db import models
from core.models import CoreModel


class Room(CoreModel):

    name = models.CharField(max_length=140)
    address = models.CharField(max_length=140)
    price = models.IntegerField(help_text="USD per night")
    beds = models.IntegerField(default=1)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    check_in = models.TimeField(default="00:00:00")
    check_out = models.TimeField(default="00:00:00")
    instant_book = models.BooleanField(default=False)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="rooms"
    )

    def __str__(self):
        return self.name

    def photo_number(self):
        return self.photos.count()

    photo_number.short_description = "Photo Count"


class Photo(CoreModel):

    file = models.ImageField()
    room = models.ForeignKey(
        "rooms.Room", related_name="photos", on_delete=models.CASCADE
    )
    caption = models.CharField(max_length=140)

    def __str__(self):
        return self.room.name
