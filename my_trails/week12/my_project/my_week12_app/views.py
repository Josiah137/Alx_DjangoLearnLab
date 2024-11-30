from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
# from .Serializers .Serlializers import BookSerializer
from .Serlializers import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()  # Fetch all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer for this view
