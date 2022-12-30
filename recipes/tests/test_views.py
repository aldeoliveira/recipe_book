from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class TestRecipesViews(TestCase):
    def test_home_view_calls_correct_function(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
