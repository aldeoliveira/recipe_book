from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe


def home(request):
    return render(request, 'recipes/pages/home.html', context={'recipes': [make_recipe() for _ in range(10)]})


def recipe(request, id):
    template = 'recipes/pages/detail.html'
    context = {
            'recipe': make_recipe(),
            'is_detail_page': True,
        }

    return render(request, template, context)
