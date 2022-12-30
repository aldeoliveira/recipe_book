from django.test import TestCase
from django.urls import reverse


class TestRecipesUrls(TestCase):
    def test_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')
