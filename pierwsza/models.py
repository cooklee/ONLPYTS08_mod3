from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)  # w db first_name varchar(100)
    last_name = models.CharField(max_length=100)  # w db last_name varchar(100)
    age = models.IntegerField()  # w db age integer


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    author = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, related_name='books_written')
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def __repr__(self):
        return str(self)

    class Meta:
        ordering = ['year', 'title']


class Tire(models.Model):
    types = [
        (1, 'Letnie'),
        (2, 'zimowe'),
        (3, 'uniwersalne')
    ]
    name = models.CharField(max_length=50)
    type = models.IntegerField(
        choices=types
    )
