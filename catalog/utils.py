"""Catalog Utils."""
import json

from django.utils.text import slugify
from operator import itemgetter

from .models import Mineral


def get_data(data_source):
    """Get the data from JSON, write to the DB and return No. of records in JSON file."""
    try:
        with open(data_source) as file:
            minerals_json = json.load(file)
            duplicate_count = Mineral.add_mineral(minerals_json)
            return {
                'minerals_json_count': len(minerals_json),
                'duplicate_count': duplicate_count
            }
    except ConnectionResetError:
        pass


def get_popular():
    """Return the fields listed in order of most used."""
    ordered_fields = [('category', len(Mineral.objects.exclude(category=''))),
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
    ordered_fields.sort(key=itemgetter(1), reverse=True)  # Sort the list
    return ordered_fields


def list_itmes():
    """
    Query the DB and return:
    - A list of groups with their full name and slug saved in a tuple.
    - A list of streaks with their full name and slug saved in a tuple.
    - A list of all mineral IDs.
    """
    groups = []
    streaks = []
    group_set = sorted(set(Mineral.objects.all().values_list('group', flat=True)))
    streak_set = sorted(set(Mineral.objects.all().values_list('streak', flat=True)))
    for group in group_set:
        groups.append((group, slugify(group)))
    for streak in streak_set:
        if streak != '':
            streaks.append((streak, slugify(streak)))
    ids = Mineral.objects.all().values_list('id', flat=True)
    return {
        'groups': groups,
        'streaks': streaks,
        'ids': ids,
        }
