"""Catalog Views."""

from django.shortcuts import render
from django.contrib import messages

from .models import Mineral
from .data_processing import get_data

def mineral_list(request):
    """Mineral list view."""
    minerals = Mineral.objects.all()
    context = {'minerals': minerals}
    return render(request, 'catalog/index.html', context)

def mineral_detail(request):
    """Mineral detail view."""
    return render(request, 'catalog/detail.html')

def import_minerals(request):
    """Import all minerals from JSON to DB."""
    minerals_json = get_data()
    context = {'minerals_json': minerals_json,}
    messages.add_message(request, messages.WARNING, 'warning')
    return render(request, 'catalog/import.html', context)