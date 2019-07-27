"""Catalog Views."""

from django.shortcuts import render

from .models import Mineral

def mineral_list(request):
    """Mineral list view."""
    return render(request, 'catalog/index.html')

def mineral_detail(request):
    """Mineral detail view."""
    return render(request, 'catalog/detail.html')
