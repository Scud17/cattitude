from django.shortcuts import render
from .models import Recipe

# Create your views here.
def recipes_list_view(request):
    qs = Recipe.objects.all()
    return render(request, 'recipes/main.html', {'qs':qs})

def recipe_detail_view(request, pk):
    obj = Recipe.objects.get(pk=pk)
    #or
    #obj = get_object_or_404(Sale, pk=pk)
    return render(request, 'recipes/detail.html', {'object':obj})