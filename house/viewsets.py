from rest_framework import viewsets

from house.models import House
from house.serializers import HouseSerializer
from house.permissions import IsHouseManagerOrNone

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    permission_classes = [IsHouseManagerOrNone,]
    serializer_class = HouseSerializer