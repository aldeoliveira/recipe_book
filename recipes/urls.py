from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

app_name = 'recipes'


urlpatterns = [
    path('recipes/<int:id>/', views.recipe, name='details'),
    path('', views.home, name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
