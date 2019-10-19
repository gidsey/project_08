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
    streak_set.pop(0)  # Remove the first empty result
    ids = all_minerals.values_list('id', flat=True)

    for group in group_set:
        groups.append((group, slugify(group)))

    for streak in streak_set:
        streaks.append((streak, slugify(streak)))

    random_mineral = random.choice(ids)

    return groups, streaks, random_mineral


# def get_groups(request):
#     """
#     Get the list of groups from the DB, remove dupliactes and sort.
#     Create a list of tuples for each: (Group, slug).
#     """
#     groups = []
#     group_set = sorted(set(models.Mineral.objects.all().values_list('group', flat=True)))
#     for group in group_set:
#         groups.append((group, slugify(group)))
#     return groups
#
#
# def get_streaks(request):
#     """
#     Get the list of streaks from the DB, remove dupliactes and sort.
#     Create a list of tuples for each: (Steak, slug).
#     """
#     streaks = []
#     streak_set = sorted(set(models.Mineral.objects.all().values_list('streak', flat=True)))
#     streak_set.pop(0)  # Remove the first empty result
#     for streak in streak_set:
#         streaks.append((streak, slugify(streak)))
#     return streaks
#
#
# def get_random_mineral_id():
#     """Return a random mineral ID."""
#     minerals = models.Mineral.objects.all().values_list('id', flat=True)
#     return random.choice(minerals)
#
