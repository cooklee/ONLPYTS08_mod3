from random import randint

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

from pierwsza.models import Person, Book, Genre


def hello(request):
    return render(request, 'base.html')


def ala(request):
    return HttpResponse("czesc jestem ala")


def przywitanie(request, imie):
    return render(request, 'przywitanie.html', {'imie': imie})


def losuj(request, liczba):
    x = randint(1, liczba)
    return render(request, 'losowanko.html', {'wylosowana': x, 'max_zakres': liczba})


def dodaj(request, l1, l2):
    return HttpResponse(l1 + l2)


def losuj_parametr(request):
    liczba = request.GET.get('liczba', 123)
    liczba = int(liczba)
    x = randint(1, liczba)
    strona = render(request, 'losowanko.html', {'wylosowana': x, 'max_zakres': liczba})
    return strona


def pokaz_parametry_get(request):
    return render(request, 'pokaz_parametry.html', {'get': request.GET})


def tabliczka_mnozenia(request, a, b):
    tab = []
    for x in range(1, a + 1):
        line = []
        for y in range(1, b + 1):
            line.append(x * y)
        tab.append(line)
    return render(request, 'tabliczka.html', {'tab': tab})


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


def all_persons(request):
    last_name = request.GET.get('last_name', '')
    persons = Person.objects.filter(last_name__icontains=last_name)
    return render(request, 'persons.html', {'persons': persons})


def all_books(request):
    title = request.GET.get('title', '')
    year = request.GET.get('year', '')
    books = Book.objects.filter(title__icontains=title)
    if year != '':
        books = books.filter(year=year)
    return render(request, 'books.html', {'books': books})


def person_detail(request, id):
    p = Person.objects.get(id=id)
    # books = Book.objects.filter(author=p) == p.book_set.all
    return render(request, 'p.html', {'person': p})


def update_person(request, id):
    p = Person.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'update_person.html', {'person': p})
    imie = request.POST['first_name']
    nazwisko = request.POST['last_name']
    wiek = request.POST['age']
    p.first_name = imie
    p.last_name = nazwisko
    p.age = wiek
    p.save()
    return render(request, 'update_person.html', {'person': p, 'message': 'udało sie'})


def add_book(request):
    persons = Person.objects.all()
    genres = Genre.objects.all()
    if request.method == "GET":
        return render(request, 'add_book.html', {'persons': persons, 'genres':genres})
    title = request.POST['title']
    year = request.POST['year']
    author_id = request.POST['author']
    genres_ids = request.POST.getlist('genre')
    p = Person.objects.get(id=author_id)
    b = Book.objects.create(title=title, year=year, author=p)
    b.genres.set(genres_ids)
    return render(request, 'add_book.html', {'persons': persons, 'book': b})


def update_book(request, id):
    persons = Person.objects.all()
    book = Book.objects.get(pk=id)
    if request.method == "GET":
        return render(request, 'update_book.html', {'persons': persons, 'book': book})
    title = request.POST['title']
    year = request.POST['year']
    author_id = request.POST['author']
    book.title_omg = title
    book.year = year
    book.author = Person.objects.get(id=author_id)
    book.save()
    return render(request, 'update_book.html', {'persons': persons, 'book': book})
