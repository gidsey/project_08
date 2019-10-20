"""Catalog Utils."""

from django.utils.text import slugify

from . import models


def list_itmes():
    """
    Query the DB and return:
    - A list of groups with their full name and slug saved in a tuple.
    - A list of streaks with their full name and slug saved in a tuple.
    - A list of all mineral IDs.
    """
    groups = []
    streaks = []
    group_set = sorted(set(models.Mineral.objects.all().values_list('group', flat=True)))
    streak_set = sorted(set(models.Mineral.objects.all().values_list('streak', flat=True)))
    for group in group_set:
        groups.append((group, slugify(group)))
    for streak in streak_set:
        if streak != '':
            streaks.append((streak, slugify(streak)))
    ids = models.Mineral.objects.all().values_list('id', flat=True)
    return {
        'groups': groups,
        'streaks': streaks,
        'ids': ids,
        }
