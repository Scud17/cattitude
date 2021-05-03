from django.urls import path
from .views import (
    recipes_list_view,
    recipe_detail_view
)

app_name = 'recipes'

urlpatterns = [
    path('all/', recipes_list_view, name='list'),
    path('<pk>', recipe_detail_view, name='details'),
]