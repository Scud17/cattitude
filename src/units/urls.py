from django.urls import path
from .views import (
    unit_list_view
)

app_name = 'units'

urlpatterns = [
    path('', unit_list_view, name='list'),
]