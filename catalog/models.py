"""Catalog Models."""

from django.db import models
from django.db import IntegrityError

from django.shortcuts import redirect


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

    def get_fields(self):
        """Returns a list of all field names on the instance."""
        field_list = []
        for field in self._meta.get_fields():
            field_list.append((field.name, getattr(self, field.name)))
            # field_list.append(field.name)
        return field_list

    @classmethod
    def add_mineral(cls, minerals):
        """Add the data."""
        errors = []
        for mineral in minerals:
            try:
                cls.objects.create(
                    name=mineral.get('name', ''),
                    image_filename=mineral.get('image_filename', ''),
                    image_caption=mineral.get('image_caption', ''),
                    category=mineral.get('category', ''),
                    formula=mineral.get('formula', ''),
                    strunz_classification=mineral.get('strunz_classification', ''),
                    color=mineral.get('color', ''),
                    crystal_system=mineral.get('crystal_system', ''),
                    unit_cell=mineral.get('unit_cell', ''),
                    crystal_symmetry=mineral.get('crystal_symmetry', ''),
                    cleavage=mineral.get('cleavage', ''),
                    mohs_scale_hardness=mineral.get('mohs_scale_hardness', ''),
                    luster=mineral.get('luster', ''),
                    streak=mineral.get('streak', ''),
                    diaphaneity=mineral.get('diaphaneity', ''),
                    optical_properties=mineral.get('optical_properties', ''),
                    refractive_index=mineral.get('refractive_index', ''),
                    crystal_habit=mineral.get('crystal_habit', ''),
                    specific_gravity=mineral.get('specific_gravity', ''),
                    group=mineral.get('group', ''),
                )
            except IntegrityError as error:
                errors.append(str(error) + ': ' + str(mineral['name']))
                # print("error: {} for {}".format(error, mineral['name']))
                pass
        print("add_mineral complete with {}".format(errors))
        return redirect('views.import_result', errors=errors)


