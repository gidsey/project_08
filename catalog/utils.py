"""Catalog Utils."""
import random

from django.utils.text import slugify

from . import models


def list_itmes(request):
    """
    :param request:
    :return:
    """
    groups = []
    streaks = []
    all_minerals = models.Mineral.objects.all()
    group_set = sorted(set(all_minerals.values_list('group', flat=True)))
    streak_set = sorted(set(all_minerals.values_list('streak', flat=True)))
    if streak_set[0] == '':
        streak_set.pop(0)  # Remove the first result (if empty)
    ids = all_minerals.values_list('id', flat=True)

    for group in group_set:
        groups.append((group, slugify(group)))

    for streak in streak_set:
        streaks.append((streak, slugify(streak)))

    random_mineral = random.choice(ids)

    return groups, streaks, random_mineral
