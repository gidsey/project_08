"""Data Processing functions."""

import json
import os

from .models import Mineral
from django.db import IntegrityError

# class Dataholder(List, data_list):
#     """Process the JSON data"""
#
#     self.data_list = data_list
#
#     def __str__(self):
#         """Return a string."""
#         return self.data_list
#


def get_data():
    """Get the data from JSON"""
    data_source = os.path.join(os.getcwd(), 'catalog/data/minerals.json')
    try:
        with open(data_source) as file:
            minerals_json = json.load(file)
            save_data(minerals_json)
            return minerals_json
    except ConnectionResetError:
        pass


def save_data(minerals_json):
    """Write to the db."""
    for mineral in minerals_json:
        print(mineral)
        try:
            Mineral.add_mineral(mineral)
        except KeyError:
            pass
        except IntegrityError:
            pass
            # raise ValueError("The mineral already exists in the database.")
