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


# def save_data(minerals_json):
#     """Write to the db."""
#     records = 0
#     recordsoutsidetryloop = 0
#
#     for mineral in minerals_json:
#         recordsoutsidetryloop +=1
#         print('recordsoutsidetryloop: {}'.format(recordsoutsidetryloop))
#         try:
#             Mineral.add_mineral(mineral)
#             records += 1
#             print ('records: {}'.format(records))
#         except KeyError as error:
#             print('error: {}'.format(error))
#             error = mineral.get('error')
#         except IntegrityError:
#             pass
#             # raise ValueError("The mineral already exists in the database.")
