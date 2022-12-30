from django.contrib import admin
from .models import Category, Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Recipe, RecipeAdmin)
