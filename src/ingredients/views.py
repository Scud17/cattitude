from django.shortcuts import render
from .models import Ingredient

# Create your views here.
def ingredients_list_view(request):
    qs = Ingredient.objects.all()
    return render(request, 'ingredients/main.html', {'qs':qs})