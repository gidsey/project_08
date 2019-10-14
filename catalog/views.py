"""Catalog Views."""

from django.shortcuts import render, get_object_or_404


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
    # minerals = Mineral.objects.all().order_by('id')
    minerals = Mineral.objects.filter(name__istartswith=name_filter).order_by('id')
    return render(request, 'catalog/index.html',
                  {'minerals': minerals})


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

