from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Book(models.Model):
    name = models.CharField(max_length=100)
    published_date = models.DateField()
    iSBN_number = models.CharField(unique=True, max_length=13)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)


