from random import randint

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

from pierwsza.models import Person


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


def add_person(request):
    if request.method == 'GET':
        return render(request, 'form.html')
    else:
        imie = request.POST['first_name']
        nazwisko = request.POST['last_name']
        wiek = request.POST['age']
        person = Person(first_name=imie, last_name=nazwisko, age=wiek)
        person.save()
    return render(request, 'podsumowanie.html')



