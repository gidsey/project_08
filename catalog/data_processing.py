"""Data Processing functions."""

import json
import os
from operator import itemgetter

from .models import Mineral


def get_data():
    """Get the data from JSON"""
    data_source = os.path.join(os.getcwd(), 'catalog/data/minerals.json')
    try:
        with open(data_source) as file:
            minerals_json = json.load(file)
            Mineral.add_mineral(minerals_json)
            return len(minerals_json)
    except ConnectionResetError:
        pass


def get_popular():
    """Return the fields listed in order of most used."""
    popular_list = [('category', len(Mineral.objects.exclude(category=''))),
                    ('formula', len(Mineral.objects.exclude(formula=''))),
                    ('strunz_classification', len(Mineral.objects.exclude(strunz_classification=''))),
                    ('color', len(Mineral.objects.exclude(color=''))),
                    ('crystal_system', len(Mineral.objects.exclude(crystal_system=''))),
                    ('unit_cell', len(Mineral.objects.exclude(unit_cell=''))),
                    ('crystal_symmetry', len(Mineral.objects.exclude(crystal_symmetry=''))),
                    ('cleavage', len(Mineral.objects.exclude(cleavage=''))),
                    ('mohs_scale_hardness', len(Mineral.objects.exclude(mohs_scale_hardness=''))),
                    ('luster', len(Mineral.objects.exclude(luster=''))),
                    ('streak', len(Mineral.objects.exclude(streak=''))),
                    ('diaphaneity', len(Mineral.objects.exclude(diaphaneity=''))),
                    ('optical_properties', len(Mineral.objects.exclude(optical_properties=''))),
                    ('refractive_index', len(Mineral.objects.exclude(refractive_index=''))),
                    ('crystal_habit', len(Mineral.objects.exclude(crystal_habit=''))),
                    ('specific_gravity', len(Mineral.objects.exclude(specific_gravity=''))),
                    ('group', len(Mineral.objects.exclude(group='')))]
    popular_list.sort(key=itemgetter(1), reverse=True)  # Sort the list
    return popular_list
