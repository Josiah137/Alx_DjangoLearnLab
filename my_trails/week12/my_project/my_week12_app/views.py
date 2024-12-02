from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
# from .Serializers .Serlializers import BookSerializer
from .Serlializers import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()  # Fetch all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer for this view (defined in the serializer.py  file)

    def get_queryset(self):
        # Get all books by default
        queryset = self.queryset
         # Allow filtering by title
        title = self.request.query_params.get('title', None) #... this return none if it can not get the requested title 
        if title: # in other words, if it is not none .....    `if title is not None:` also works 
            #filtering with the requested title name from our queryset(all the books)
            queryset = queryset.filter(title__icontains=title) 

        # Filter by author (optional)
        author = self.request.query_params.get('author', None)
        if author:
            queryset = queryset.filter(author__icontains=author)

        return queryset
    