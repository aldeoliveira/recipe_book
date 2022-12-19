from django.urls import path
from . import views

app_name = 'recipes'


urlpatterns = [
    path('recipes/<int:id>/', views.recipe, name='details'),
    path('', views.home, name='home'),
]
