"""Catalog Utils."""
import random

from django.utils.text import slugify

from . import models


def get_groups(request):
    """
    Get the list of groups from the DB, remove dupliactes and sort.
    Create a list of tuples for each: (Group, slug).
    """
    groups = []
    group_set = sorted(set(models.Mineral.objects.all().values_list('group', flat=True)))
    for group in group_set:
        groups.append((group, slugify(group)))
    return groups


def get_streaks(request):
    """
    Get the list of streaks from the DB, remove dupliactes and sort.
    Create a list of tuples for each: (Steak, slug).
    """
    streaks = []
    streak_set = sorted(set(models.Mineral.objects.all().values_list('streak', flat=True)))
    streak_set.pop(0)  # Remove the first empty result
    for streak in streak_set:
        streaks.append((streak, slugify(streak)))
    return streaks


def get_random_mineral_id():
    """Return a random mineral ID."""
    minerals = models.Mineral.objects.all().values_list('id', flat=True)
    return random.choice(minerals)

