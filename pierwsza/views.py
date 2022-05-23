from random import randint

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError


def hello(request):
    return render(request, 'base.html')

def ala(request):
    return HttpResponse("czesc jestem ala")

def przywitanie(request, imie):
    return render(request, 'przywitanie.html', {'imie':imie})

def losuj(request, liczba):
    x = randint(1, liczba)
    return render(request, 'losowanko.html', {'wylosowana':x, 'max_zakres':liczba})

def dodaj(request, l1, l2):
    return HttpResponse(l1+l2)

def losuj_parametr(request):

    liczba = request.GET.get('liczba', 123)
    liczba = int(liczba)
    x = randint(1, liczba)
    return render(request, 'losowanko.html', {'wylosowana': x, 'max_zakres': liczba})

def pokaz_parametry_get(request):
    return render(request, 'pokaz_parametry.html', {'get':request.GET})


def tabliczka_mnozenia(request, a, b):
    tab = []
    for x in range(1, a+1):
        line = []
        for y in range(1, b+1):
            line.append(x*y)
        tab.append(line)
    return render(request, 'tabliczka.html', {'tab':tab})






