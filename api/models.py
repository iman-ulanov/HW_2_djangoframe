from django.db import models


class Position(models.Model):
    branch = models.CharField(max_length=30)
    position = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.position}'


class Employee(models.Model):
    name = models.CharField(max_length=40)
    birth_date = models.DateField()
    position = models.IntegerField()
    salary = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.position}'

