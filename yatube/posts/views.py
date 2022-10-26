from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Здесь пока ничего нет, но скоро будет потрясающе!)')


def group_posts(request, slug):
    return HttpResponse(f'Пост номер {slug} (Нет)')
