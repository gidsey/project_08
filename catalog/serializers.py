from rest_framework import serializers

from . import models


class MineralSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'image_filename',
            'image_caption',
            'category',
            'formula',
            'strunz_classification',
            'color',
            'crystal_system',
            'unit_cell',
            'crystal_symmetry',
            'cleavage',
            'mohs_scale_hardness',
            'luster',
            'streak',
            'diaphaneity',
            'optical_properties',
            'refractive_index',
            'crystal_habit',
            'specific_gravity',
            'group',
        )
        model = models.Mineral
