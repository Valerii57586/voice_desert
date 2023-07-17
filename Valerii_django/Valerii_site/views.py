from django.shortcuts import render
from django.http import HttpResponse
from .models import Car

def index(request):
    template = 'index.html'
    cars = Car.objects.all()
    title = 'надпись наверху'
    context = {
        'title':title,
        'cars':cars
    }
    
    return render(request, template, context)


def all_site(request):
    return HttpResponse('Страница сайтов')


def only_site(request, pk):
    return HttpResponse(f'Страница сайтов number {pk}')
