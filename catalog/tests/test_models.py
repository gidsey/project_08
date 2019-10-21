from django.test import TestCase
from catalog.models import Mineral


class MineralModelTests(TestCase):
    """Test the Mineral model."""
    def setUp(self):
        Mineral.objects.create(
            name="Axinite",
            image_filename="Axinite.jpg",
            streak="White to greyish white",
            group='Silicates'
        )
        Mineral.objects.create(
            name="Barstowite",
            image_filename="Barstowite.jpg",
            streak="White to brownish",
            group='Organic Minerals'
        )

    def test_mineral_name(self):
        """Test mineral name is set correctly"""
        axinite = Mineral.objects.get(name='Axinite')
        barstowite = Mineral.objects.get(name='Barstowite')
        self.assertEqual(str(axinite), 'Axinite')
        self.assertEqual(str(barstowite), 'Barstowite')

    def test_mineral_group(self):
        """Test mineral group is set correctly"""
        axinite = Mineral.objects.get(name='Axinite')
        barstowite = Mineral.objects.get(name='Barstowite')
        self.assertEqual(axinite.group, 'Silicates')
        self.assertEqual(barstowite.group, 'Organic Minerals')