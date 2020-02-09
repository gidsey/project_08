from rest_framework import serializers

from . import models


class MineralSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'image_filename',
            'image_caption',
        )
        model = models.Mineral
