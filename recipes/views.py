from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', status=201, context={
        'name': 'Victor Kakiuti',
    })


def contato(request):
    return render(request, 'me_apague/temp.html')


def sobre(request):
    return HttpResponse('sobre 1')
