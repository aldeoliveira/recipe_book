from django.test import TestCase
from django.urls import reverse, resolve
from . import views


class TestRecipesUrls(TestCase):
    def test_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')


class TestRecipesViews(TestCase):
    def test_home_view_calls_correct_function(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
