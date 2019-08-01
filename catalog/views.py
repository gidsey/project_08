"""Catalog Views."""

from django.shortcuts import render, get_object_or_404


from .models import Mineral
from .data_processing import get_data, get_popular

def mineral_list(request):
    """Mineral list view."""
    minerals = Mineral.objects.all().order_by('id')
    context = {'minerals': minerals}
    return render(request, 'catalog/index.html', context)

def mineral_detail(request, pk):
    """Mineral detail view."""
    mineral = get_object_or_404(Mineral, pk=pk)
    field_list = mineral.get_fields()
    return render(request, 'catalog/detail.html',
                  {'mineral': mineral, 'field_list': field_list})

def import_minerals(request):
    """Import all minerals from JSON to DB."""
    minerals_json_count = get_data()
    minerals = Mineral.objects.all().order_by('id')
    field_popularity = get_popular()
    return render(request, 'catalog/import.html',
                  {'minerals_json_count': minerals_json_count,
                   'minerals': minerals,
                   'field_popularity': field_popularity})

# def import_result(request, errors):
#     """Show the results of the import including any errors"""
#     context = {'errors': errors}
#     return render(request, 'catalog/import_result.html', context)