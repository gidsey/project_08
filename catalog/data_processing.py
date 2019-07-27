"""Data Processing functions."""

import json
import os

def get_data():
	"""Get the data from JSON"""
	data_source = os.path.join(os.getcwd(), 'catalog/data/minerals.json')
	with open(data_source) as mineralsfile:
		minerals = json.load(mineralsfile)
		return minerals