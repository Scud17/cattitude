from django.shortcuts import render
from .models import Unit

# Create your views here.
def unit_list_view(request):
    query_set_units = Unit.objects.all()
    context = {
        'qs': query_set_units
        }
    return render(request, "units/main.html", context)
