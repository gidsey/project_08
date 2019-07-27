"""Catalog Models."""

from django.db import models

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
        for mineral in minerals:
            try:
                cls.create(
                    name=mineral.name,
                    image_filename=mineral.image_filename,
                    image_caption=mineral.image_caption,
                    category=mineral.category,
                    formula=mineral.formula,
                    strunz_classification=mineral.strunz_classification,
                    color=mineral.color,
                    crystal_system=mineral.crystal_system,
                    unit_cell=mineral.unit_cell,
                    crystal_symmetry=mineral.crystal_symmetry,
                    cleavage=mineral.cleavage,
                    mohs_scale_hardness=mineral.mohs_scale_hardness,
                    luster=mineral.luster,
                    streak=mineral.streak,
                    diaphaneity=mineral.diaphaneity,
                    optical_properties=mineral.optical_properties,
                    refractive_index=mineral.refractive_index,
                    crystal_habit=mineral.crystal_habit,
                    specific_gravity=mineral.specific_gravity,
                    group=mineral.group,
            )
            except IntegrityError:
                raise ValueError("Mineral already exists")

