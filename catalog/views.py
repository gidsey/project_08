"""Catalog Views."""

from django.shortcuts import render, get_object_or_404
from django.db.models import Count

from .models import Mineral
from .data_processing import get_data, get_popular


def import_minerals(request):
    """Import all minerals from JSON to DB."""
    data = get_data()
    minerals_json_count = data[0]
    duplicate_count = data[1]
    minerals = Mineral.objects.all().order_by('id')
    ordered_fields = get_popular()
    request.session['ordered_fields'] = ordered_fields
    return render(request, 'catalog/import.html',
                  {'minerals_json_count': minerals_json_count,
                   'duplicate_count': duplicate_count,
                   'minerals': minerals,
                   'ordered_fields': ordered_fields})


def mineral_list(request, name_filter=None):
    """Mineral list view."""
    if name_filter is None:
        name_filter = 'a'
    minerals = Mineral.objects.all()
    mineral_filtered = Mineral.objects.filter(name__istartswith=name_filter).order_by('id')
    return render(request, 'catalog/index.html',{
        'minerals': minerals,
        'mineral_filtered': mineral_filtered,
    })


def mineral_group(request, group_filter):
    """Mineral Group view."""
    minerals = Mineral.objects.all()
    mineral_filtered = Mineral.objects.filter(group__iexact=group_filter).order_by('id')
    num_in_group = mineral_filtered.count()
    return render(request, 'catalog/index.html',{
        'minerals': minerals,
        'mineral_filtered': mineral_filtered,
        'group_filter': group_filter,
        'num_in_group': num_in_group,
    })


def mineral_detail(request, pk):
    """Mineral detail view."""
    mineral = get_object_or_404(Mineral, pk=pk)
    if 'ordered_fields' not in request.session:
        ordered_fields = get_popular()
        request.session['ordered_fields'] = ordered_fields
    else:
        ordered_fields = request.session['ordered_fields']
    field_list = mineral.get_fields(ordered_fields)
    return render(request, 'catalog/detail.html',
                  {'mineral': mineral, 'field_list': field_list})


def search(request):
    """Define the search view."""
    term = request.GET.get('q')
    minerals = Mineral.objects.all()
    mineral_filtered = Mineral.objects.filter(name__icontains=term)
    num_results = mineral_filtered.count()
    return render(request, 'catalog/index.html', {
        'minerals': minerals,
        'mineral_filtered': mineral_filtered,
        'num_results': num_results,
        'term': term,
    })
