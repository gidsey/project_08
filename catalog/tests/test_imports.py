from django.test import TestCase
import os
from catalog.utils import get_data


class ImportDataTests(TestCase):

    def setUp(self):
        self.data_souce = os.path.join(os.getcwd(), 'catalog/data/test.json')

    def test_get_data(self):
        """
        Import test JSON file and check for
        number of items and
        number of duplicates
        """
        test_data = get_data(self.data_souce)
        self.assertEqual(test_data['minerals_json_count'], 10)
        self.assertEqual(test_data['duplicate_count'], 1)

