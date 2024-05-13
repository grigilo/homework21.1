from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Product


# def index(request):
#     #return render(request, 'catalog/index.html')
#     return render(request, 'base.html')

# def product_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, 'product_list.html', context)
class ProductListView(ListView):
    model = Product

    # app_name/<model_name>_<action>
    # catalog/product_list.html


class ProductDetailView(DetailView):
    model = Product


# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#
#         print(f'{name} ({email}): {message}')
#     return render(request, 'catalog/contact.html')


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, 'product_detail.html', context)
