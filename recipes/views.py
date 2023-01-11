from django.shortcuts import render
from utils.recipes.factory import make_recipe

from .models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={'recipes': recipes})


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={'recipes': recipes})
    # TODO: if the cover image is not big enough, there is a margin left on the card in this template
    # TODO: change main logo text when in category as oposed to home


def recipe(request, id):
    template = 'recipes/pages/detail.html'
    context = {
            'recipe': make_recipe(),
            'is_detail_page': True,
        }

    return render(request, template, context)
