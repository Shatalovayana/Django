from django.shortcuts import render

from catalog.models import Product


def index(request):
    product_list = Product.objects.all()
    context = {
        "object_list": product_list
    }
    return render(request, 'catalog/index.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}, {message}')
    return render(request, 'catalog/contact.html')


def product(request, pk):
    product_object = Product.objects.get(pk=pk)
    return render(request, 'catalog/products.html', {'object': product_object})
