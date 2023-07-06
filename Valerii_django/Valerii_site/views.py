from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Валерий лев, тигр, пантера, а Даниелян Сергей петух')


def all_site(request):
    return HttpResponse('Страница сайтов')
