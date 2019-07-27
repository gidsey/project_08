"""Data Processing functions."""

import json
import os

from .models import Mineral

def get_data():
	"""Get the data from JSON"""
	data_source = os.path.join(os.getcwd(), 'catalog/data/minerals.json')
	try:
		with open(data_source) as file:
			minerals = json.load(file)
			Mineral.add_mineral(minerals)
		return minerals
	except ConnectionResetError:
		pass
