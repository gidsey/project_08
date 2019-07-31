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
    pop_list = []
    count_list = []
    mineral_fields = Mineral._meta.get_fields()
    for field in mineral_fields:
        pop_list.append(field.name)
    for f in pop_list:
        count_list.append(f)
    return count_list
