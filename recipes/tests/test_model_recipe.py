from django.test import TestCase
from unittest import skip


class TestModelRecipe(TestCase):
    @skip('test is not ready')
    def test_title_max_length_is_65_chars(self):
        pass
    
    @skip('test is not ready')
    def test_description_max_length_is_165_chars(self):
        pass

    @skip('test is not ready')
    def test_slug_is_correct(self):
        pass

    @skip('test is not ready')
    def test_preparation_steps_is_html_is_false_by_default(self):
        pass

    @skip('test is not ready')
    def test_created_at_is_automatically_set_when_recipe_is_created(self):
        pass

    @skip('test is not ready')
    def test_created_at_does_not_change_when_recipe_is_updated(self):
        pass

    @skip('test is not ready')
    def test_updated_at_is_set_everytime_the_recipe_is_updated(self):
        pass

    @skip('test is not ready')
    def test_cover_image_is_saved_into_the_correct_folder(self):
        pass

    @skip('test is not ready')
    def test_field_category_relates_to_model_category(self):
        pass

    @skip('test is not ready')
    def test_field_author_relates_to_model_user(self):
        pass
