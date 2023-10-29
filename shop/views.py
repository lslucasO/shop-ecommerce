from django.shortcuts import render


def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'shop/pages/home.html', context)


def products(request):
    context = {
        'title': 'Products'
    }
    return render(request, 'shop/pages/products.html', context)