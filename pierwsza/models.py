from django.db import models




class Person(models.Model):
    first_name = models.CharField(max_length=100)  # w db first_name varchar(100)
    last_name = models.CharField(max_length=100)   # w db last_name varchar(100)
    age = models.IntegerField()                    # w db age integer



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
