"""Catalog Views."""
import random
import os

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from . import utils
from .models import Mineral

# CONSTANTS
DATA_SOURCE = os.path.join(os.getcwd(), 'catalog/data/minerals.json')
# Get the ORDERED_FIELDS, GROUPS, STREAKS and IDS once and save them as constants.
ORDERED_FIELDS = utils.get_popular()
list_items = utils.list_itmes()
GROUPS = list_items['groups']
STREAKS = list_items['streaks']
IDS = list_items['ids']


def check_data(request):
    """Check if the database contains data and redirect accordingly"""
    minerals = Mineral.objects.all().order_by('id')
    if minerals:
        return HttpResponseRedirect('/list')
    else:
        return render(request, 'catalog/no-data.html', {'import': True, })


def import_minerals(request):
    """Import all minerals from JSON to DB."""
    data = utils.get_data(DATA_SOURCE)
    minerals_json_count = data['minerals_json_count']
    duplicate_count = data['duplicate_count']
    minerals = Mineral.objects.all().order_by('id')
    return render(request, 'catalog/import.html',
                  {'import': True,
                   'minerals_json_count': minerals_json_count,
                   'duplicate_count': duplicate_count,
                   'minerals': minerals,
                   'ordered_fields': ORDERED_FIELDS})


def mineral_list(request, name_filter='a'):
    """Mineral list view."""
    mineral_filtered = Mineral.objects.filter(name__istartswith=name_filter).order_by('id')
    num_in_list = mineral_filtered.count()
    random_mineral = random.choice(IDS)
    return render(request, 'catalog/list.html', {
        'name_filter': name_filter,
        'mineral_filtered': mineral_filtered,
        'num_in_list': num_in_list,
        'groups': GROUPS,
        'streaks': STREAKS,
        'random_mineral': random_mineral,
    })


def mineral_group(request, group_filter):
    """Mineral Group view."""
    random_mineral = random.choice(IDS)
    search_term = [item[0] for item in GROUPS if group_filter in item][0]  # Get the de-slugified search term
    mineral_filtered = Mineral.objects.filter(group__iexact=search_term).order_by('id')
    num_in_group = mineral_filtered.count()

    return render(request, 'catalog/list.html', {
        'search_term': search_term,
        'mineral_filtered': mineral_filtered,
        'groups': GROUPS,
        'streaks': STREAKS,
        'num_in_group': num_in_group,
        'random_mineral': random_mineral,
    })


def mineral_streak(request, streak_filter):
    """Mineral Streak view."""
    random_mineral = random.choice(IDS)
    search_term = [item[0] for item in STREAKS if streak_filter in item][0]  # Get the de-slugified search term
    mineral_filtered = Mineral.objects.filter(streak__iexact=search_term).order_by('id')
    num_in_group = mineral_filtered.count()

    return render(request, 'catalog/list.html', {
        'search_term': search_term,
        'mineral_filtered': mineral_filtered,
        'groups': GROUPS,
        'streaks': STREAKS,
        'num_in_group': num_in_group,
        'random_mineral': random_mineral,
    })


def mineral_detail(request, pk):
    """Mineral detail view."""
    random_mineral = random.choice(IDS)
    mineral = get_object_or_404(Mineral, pk=pk)
    field_list = mineral.get_fields(ORDERED_FIELDS)
    return render(request, 'catalog/detail.html', {
                'mineral': mineral,
                'field_list': field_list,
                'groups': GROUPS,
                'streaks': STREAKS,
                'random_mineral': random_mineral,
    })


def search(request):
    """Search view. Perform a keyword serach across all fields."""
    random_mineral = random.choice(IDS)
    term = request.GET.get('q')
    mineral_filtered = Mineral.objects.filter(
        Q(name__icontains=term) |
        Q(image_filename__icontains=term) |
        Q(image_caption__icontains=term) |
        Q(category__icontains=term) |
        Q(formula__icontains=term) |
        Q(strunz_classification__icontains=term) |
        Q(color__icontains=term) |
        Q(crystal_system__icontains=term) |
        Q(unit_cell__icontains=term) |
        Q(crystal_symmetry__icontains=term) |
        Q(cleavage__icontains=term) |
        Q(mohs_scale_hardness__icontains=term) |
        Q(luster__icontains=term) |
        Q(streak__icontains=term) |
        Q(diaphaneity__icontains=term) |
        Q(optical_properties__icontains=term) |
        Q(refractive_index__icontains=term) |
        Q(crystal_habit__icontains=term) |
        Q(specific_gravity__icontains=term) |
        Q(group__icontains=term)
    )
    num_results = mineral_filtered.count()
    return render(request, 'catalog/list.html', {
        'mineral_filtered': mineral_filtered,
        'num_results': num_results,
        'term': term,
        'groups': GROUPS,
        'streaks': STREAKS,
        'random_mineral': random_mineral,
    })
