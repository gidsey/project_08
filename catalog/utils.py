"""Catalog Utils."""
import random

from . import models


def get_groups():
    """Get the list of groups from the DB, remove dupliactes and sort."""
    return sorted(set(models.Mineral.objects.all().values_list('group', flat=True)))


def get_streaks():
    """Get the list of streaks from the DB, remove dupliactes, empty items and sort."""
    streaks = sorted(set(models.Mineral.objects.all().values_list('streak', flat=True)))
    streaks.pop(0)
    return streaks


def get_random_mineral_id():
    """Return a random mineral ID."""
    minerals = models.Mineral.objects.all().values_list('id', flat=True)
    return random.choice(minerals)
