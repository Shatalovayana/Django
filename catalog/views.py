from django.shortcuts import render

from catalog.models import Product


def index(request):
    return render(request, 'catalog/index.html')


def products(request):
    product_list = Product.objects.all()
    context = {
        "object_list": product_list
    }
    return render(request, 'catalog/products.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}, {message}')
    return render(request, 'catalog/contact.html')
