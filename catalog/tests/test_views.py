from django.test import RequestFactory, TestCase

from catalog.models import Mineral
from catalog import views


class MineralViewsTests(TestCase):
    """Test the views."""

    def setUp(self):
        #  Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.axinite = Mineral.objects.create(
            name="Axinite",
            image_filename="Axinite.jpg",
            streak="White to greyish white",
            group='Silicates'
        )
        self.barstowite = Mineral.objects.create(
            name="Barstowite",
            image_filename="Barstowite.jpg",
            streak="White to brownish",
            group='Organic Minerals',
        )

    def test_letter_filter_view(self):
        """
        Letter filter must show minerals that start with the selected letter only.
        letter 'b' used as filter
        """
        request = self.factory.get('list/letter/')
        response = views.mineral_list(request, **{'name_filter': 'b'})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, self.axinite.name)
        self.assertContains(response, self.barstowite.name)

    def test_groups_filter_view(self):
        """
        Group filter must show minerals by selected group only.
        'organic-minerals' used as slugified filter
        """

        request = self.factory.get('list/group/')
        response = views.mineral_group(request, **{'group_filter': 'organic-minerals'})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, self.axinite.name)
        self.assertContains(response, self.barstowite.name)

    def test_streak_filter_view(self):
        """
        Streak filter must show minerals with selected streak only.
        'white-to-greyish-white' used as slugified filter
        """
        request = self.factory.get('list/group/')
        response = views.mineral_streak(request, **{'streak_filter': 'white-to-greyish-white'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.axinite.name)
        self.assertNotContains(response, self.barstowite.name)

    def test_search_view(self):
        """
        Keyword Search across all fields
        'Greyish' used as serach term
        """
        request = self.factory.get('search/', {'q': 'Greyish'})
        response = views.search(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.axinite.name)
        self.assertNotContains(response, self.barstowite.name)

    def test_mineral_detail_view(self):
        """
        Test the detail view
        """
        request = self.factory.get('detail/')
        response = views.mineral_detail(request, **{'pk':  self.barstowite.pk})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.barstowite.name)
        self.assertContains(response, self.barstowite.image_filename)
        self.assertContains(response, self.barstowite.streak)
        self.assertContains(response, self.barstowite.group)