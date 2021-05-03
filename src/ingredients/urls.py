from django.urls import path
from .views import (
    ingredients_list_view,
)

app_name = 'ingredients'

urlpatterns = [
    path('all/', ingredients_list_view, name='list')
]