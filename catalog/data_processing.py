"""Data Processing functions."""

import json
import os

from .models import Mineral


def get_data():
    """Get the data from JSON"""
    data_source = os.path.join(os.getcwd(), 'catalog/data/minerals.json')
    try:
        with open(data_source) as file:
            minerals_json = json.load(file)
            Mineral.add_mineral(minerals_json)
            return minerals_json
    except ConnectionResetError:
        pass


def get_popular():
    """Return the fields listed in order of most used."""

    popular_list=[({'category': len(Mineral.objects.exclude(category=''))})]
    popular_list.append({'color': len(Mineral.objects.exclude(color=''))})
    popular_list.append({'specific_gravity': len(Mineral.objects.exclude(specific_gravity=''))})
    return popular_list
