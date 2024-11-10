from .models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()  # Using the related name "books"
        return books
    except Author.DoesNotExist:
        return None

# 2. List all books in a specific library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Using the related name "books"
        return books
    except Library.DoesNotExist:
        return None

# 3. Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # Using the related name "librarian"
        return librarian
    except Library.DoesNotExist:
        return None
