from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from .forms import ProductsSearchForm

# Create your views here.
def home_view(request):
    form = ProductsSearchForm(request.POST or None)
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        print(date_from, date_to, chart_type)

        qs = Product.objects.filter(created_ts__date=date_from)
        print(qs)

    context = {
        'form': form,
    }
    return render(request, 'products/home.html', context)

def products_list_view(request):
    qs = Product.objects.all()
    return render(request, 'products/main.html', {'qs':qs})

def product_detail_view(request, pk):
    obj = Product.objects.get(pk=pk)
    #or
    #obj = get_object_or_404(Sale, pk=pk)
    return render(request, 'products/detail.html', {'object':obj})