from rest_framework import viewsets
from .models import Room
from .serializers import BigRoomSerializer


class RoomViewset(viewsets.ModelViewSet):

    queryset = Room.objects.all()
    serializer_class = BigRoomSerializer
