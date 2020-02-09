from rest_framework import viewsets

from . import models
from . import serializers


class MineralViewSet(viewsets.ModelViewSet):
    queryset = models.Mineral.objects.all()
    serializer_class = serializers.MineralSerializer

