"""Tests."""

from django.test import TestCase
from django.urls import reverse

from .models import Mineral


class MineralModelTests(TestCase):
    """Test the Course Model."""

    def test_course_creation(self):
        """Create a course and test the filename contains '.jpg'"""
        mineral = Mineral.objects.create(
            name="Abernathyite",
            image_filename="Abernathyite.jpg",
            group='other'
        )
        self.assertIn('.jpg', mineral.image_filename)


class MineralViewsTests(TestCase):
    """Test the views."""

    def setUp(self):
        """Setup."""
        self.mineral = Mineral.objects.create(
            name="Sellaite",
            image_filename="Sellaite.jpg",
            image_caption="Sellaite crystal from Serra das \u00c9guas, Brazil (size: 4.2 x 2.4 x 2 cm)",
            category="Halide",
            formula="MgF<sub>2</sub>",
            strunz_classification="3.AB.15",
            crystal_system="Tetragonal",
            unit_cell="a = 4.6213(2) \u00c5, c = 3.0519(1) \u00c5; Z=2",
            color="Colorless to white",
            crystal_symmetry="Tetragonal, ditetragonal dipyramidalH-M symbol: (4/m 2/m 2/m)Space group: P 41/mnm",
            cleavage="Perfect on {010} and {110}",
            mohs_scale_hardness="5\u20135.5",
            luster="Vitreous",
            streak="black",
            diaphaneity="Transparent",
            optical_properties="Uniaxial (+)",
            refractive_index="n\u03c9 = 1.378 n\u03b5 = 1.390",
            crystal_habit="Prismatic crystals; fibrous, radial, spherulitic",
            specific_gravity="3.15",
            group="Halides"
        )
        self.mineral2 = Mineral.objects.create(
            name="Zunyite",
            image_filename="Zunyite.jpg",
            image_caption="Zunyite crystal from Serra das \u00c9guas, Brazil (size: 4.2 x 2.4 x 2 cm)",
            category="Halide",
            formula="MgF<sub>2</sub>",
            strunz_classification="3.AB.15",
            crystal_system="Tetragonal",
            unit_cell="a = 4.6213(2) \u00c5, c = 3.0519(1) \u00c5; Z=2",
            color="Colorless to white, blue",
            cleavage="Perfect on {010} and {110}",
            mohs_scale_hardness="5\u20135.5",
            luster="Vitreous",
            streak="black",
            diaphaneity="Transparent",
            optical_properties="Uniaxial (+)",
            refractive_index="n\u03c9 = 1.378 n\u03b5 = 1.390",
            crystal_habit="Prismatic crystals; fibrous, radial, spherulitic",
            specific_gravity="3.15",
            group="Halides"
        )

    def test_letter_filter_view(self):
        """Test the letter filter view."""
        resp = self.client.get(reverse('catalog:filtered_list',
                                       kwargs={'name_filter': 's'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['mineral_filtered'])
        self.assertTemplateUsed(resp, 'catalog/list.html')
        self.assertContains(resp, self.mineral.name)


    def test_group_filter_view(self):
        """Test the Group filter view."""
        resp = self.client.get(reverse('catalog:group_list',
                                       kwargs={'group_filter': 'Halides'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral2, resp.context['mineral_filtered'])
        self.assertTemplateUsed(resp, 'catalog/list.html')
        self.assertContains(resp, self.mineral2.name)


    def test_streak_filter_view(self):
        """Test the Streak filter view."""
        resp = self.client.get(reverse('catalog:streak_list',
                                       kwargs={'streak_filter': 'black'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['mineral_filtered'])
        self.assertIn(self.mineral2, resp.context['mineral_filtered'])
        self.assertTemplateUsed(resp, 'catalog/list.html')
        self.assertContains(resp, self.mineral.name)


    def test_search(self):
        """Test the Streak filter view."""
        resp = self.client.get(reverse('catalog:search', "q=joe"))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['mineral_filtered'])
        self.assertTemplateUsed(resp, 'catalog/list.html')
        self.assertContains(resp, self.mineral.name)



    def test_detail_view(self):
        """Test the detail view."""
        resp = self.client.get(reverse('catalog:detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'catalog/detail.html')
        self.assertContains(resp, self.mineral.group)

    def test_import_view(self):
        """Test the index view."""
        resp = self.client.get(reverse('catalog:import'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'catalog/import.html')
