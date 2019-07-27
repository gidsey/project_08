"""Catalog Models."""

from django.db import models
from django.db import IntegrityError

class Mineral(models.Model):
    """Define the Mineral model."""
    name = models.CharField(max_length=255, unique=True)
    image_filename = models.CharField(max_length=255)
    image_caption = models.TextField()
    category = models.CharField(max_length=255)
    formula = models.CharField(max_length=255)
    strunz_classification = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    crystal_system = models.CharField(max_length=255)
    unit_cell = models.CharField(max_length=255)
    crystal_symmetry = models.CharField(max_length=255)
    cleavage = models.CharField(max_length=255)
    mohs_scale_hardness = models.CharField(max_length=255)
    luster = models.CharField(max_length=255)
    streak = models.CharField(max_length=255)
    diaphaneity = models.CharField(max_length=255)
    optical_properties = models.CharField(max_length=255)
    refractive_index = models.CharField(max_length=255)
    crystal_habit = models.CharField(max_length=255)
    specific_gravity = models.CharField(max_length=255)
    group = models.CharField(max_length=255)

    def __str__(self):
        """Define the str."""
        return self.name

    class Meta:
        """Define the ordering."""

        ordering = ['name']

    @classmethod
    def add_mineral(cls, minerals):
        """Add the data."""
        optical_properties = None
        for mineral in minerals:
            if mineral['optical_properties']:
                optical_properties = mineral['optical_properties']
            else:
                optical_properties = None
        print(optical_properties)


        for mineral in minerals:
            if mineral['name']:
                name = mineral['name']
            if mineral['image_filename']:
                image_filename = mineral['image_filename']
            if mineral['image_caption']:
                image_caption = mineral['image_caption']
            if mineral['category']:
                category = mineral['category']
            if mineral['formula']:
                formula = mineral['formula']
            if mineral['strunz_classification']:
                strunz_classification = mineral['strunz_classification']
            if mineral['color']:
                color = mineral['color']
            if mineral['crystal_system']:
                crystal_system = mineral['crystal_system']
            if mineral['unit_cell']:
                unit_cell = mineral['unit_cell']
            if mineral['crystal_symmetry']:
                crystal_symmetry = mineral['crystal_symmetry']
            if mineral['cleavage']:
                cleavage = mineral['cleavage']
            if mineral['mohs_scale_hardness']:
                mohs_scale_hardness = mineral['mohs_scale_hardness']
            if mineral['luster']:
                luster = mineral['luster']
            if mineral['streak']:
                streak = mineral['streak']
            if mineral['diaphaneity']:
                diaphaneity = mineral['diaphaneity']
            if mineral['optical_properties']:
                optical_properties = mineral['optical_properties']
            if mineral['refractive_index']:
                refractive_index = mineral['refractive_index']
            if mineral['crystal_habit']:
                crystal_habit = mineral['crystal_habit']
            if mineral['specific_gravity']:
                specific_gravity = mineral['specific_gravity']
            if mineral['group']:
                group = mineral['group']

            try:
                cls.objects.create(
                    name=name,
                    image_filename=image_filename,
                    image_caption=image_caption,
                    category=category,
                    formula=formula,
                    strunz_classification=strunz_classification,
                    color=color,
                    crystal_system=crystal_system,
                    unit_cell=unit_cell,
                    crystal_symmetry=crystal_symmetry,
                    cleavage=cleavage,
                    mohs_scale_hardness=mohs_scale_hardness,
                    luster=luster,
                    streak=streak,
                    diaphaneity=diaphaneity,
                    optical_properties=optical_properties,
                    refractive_index=refractive_index,
                    crystal_habit=crystal_habit,
                    specific_gravity=specific_gravity,
                    group=group,
            )
            except IntegrityError:
                raise ValueError("Mineral already exists")

