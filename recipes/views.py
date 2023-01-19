from django.shortcuts import render, get_list_or_404
from utils.recipes.factory import make_recipe

from .models import Recipe


def home(request):
    template = 'recipes/pages/home.html'
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    context = {'recipes': recipes}

    return render(request, template, context)


def category(request, category_id):
    template = 'recipes/pages/category.html'
    queryset = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    recipes = get_list_or_404(queryset)
    title = f'{recipes[0].category.name} - Category | '
    context = {'recipes': recipes, 'title': title}

    return render(request, template, context)

    # TODO: if the cover image is not big enough, there is a margin left on the card in this template
    # TODO: change main logo text when in category as oposed to home


def recipe(request, id):
    template = 'recipes/pages/detail.html'
    context = {
            'recipe': make_recipe(),
            'is_detail_page': True,
        }

    return render(request, template, context)
