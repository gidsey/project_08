"""Catalog Utils."""
import random

from django.utils.text import slugify

from . import models


def get_groups(request):
    """Get the list of groups from the DB, remove dupliactes and sort.
    Store in a session varable and retieve as required."""
    if 'groups' not in request.session:
        groups = []
        group_set = sorted(set(models.Mineral.objects.all().values_list('group', flat=True)))
        for group in group_set:
            groups.append((group, slugify(group)))
        request.session['groups'] = groups
    else:
        groups = request.session['groups']
    return groups


def get_streaks(request):
    """Get the list of streaks from the DB, remove dupliactes and sort.
    Store in a session varable and retieve as required."""
    if 'streaks' not in request.session:
        streaks = sorted(set(models.Mineral.objects.all().values_list('streak', flat=True)))
        streaks.pop(0)
        request.session['streaks'] = streaks
    else:
        streaks = request.session['streaks']
    return streaks


def get_random_mineral_id():
    """Return a random mineral ID."""
    minerals = models.Mineral.objects.all().values_list('id', flat=True)
    return random.choice(minerals)

