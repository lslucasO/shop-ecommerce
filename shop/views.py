from django.shortcuts import render


def home(request):
    return render(request, 'shop/pages/home.html')