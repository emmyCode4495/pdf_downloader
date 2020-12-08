from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return render(request,'Landing_page/home.html')


def about_page(request):
    return render(request, 'Landing_page/about.html')