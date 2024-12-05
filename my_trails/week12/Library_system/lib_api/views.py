from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .models import Book, Author, Genre
from .Serializator import AuthorSerializer, GenreSerializers, BookSerializers

#settting app all instances and their respective serilizer
class Bookviewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers