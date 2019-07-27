"""Catalog Views."""

from django.shortcuts import render

from .models import Mineral
from .data_processing import get_data

def mineral_list(request):
    """Mineral list view."""
    return render(request, 'catalog/index.html')

def mineral_detail(request):
    """Mineral detail view."""
    return render(request, 'catalog/detail.html')

def import_minerals(request):
    """Import all minerals from JSON to DB."""
    context = {'minerals': get_data()}
    return render(request, 'catalog/import.html', context)