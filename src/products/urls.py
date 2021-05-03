from django.urls import path
from .views import (
    home_view,
    products_list_view,
    product_detail_view
)

app_name = 'products'

urlpatterns = [
    path('all/', products_list_view, name='list'),
    path('<pk>', product_detail_view, name='details'),
]