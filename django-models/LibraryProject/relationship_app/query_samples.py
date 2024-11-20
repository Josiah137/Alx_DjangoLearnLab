import os
import sys
import django

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()


from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author):
    try:
        author = Author.objects.get(name=author)
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
        librarian = library.librarians# Using the related name "librarian"
        return librarian
    except Library.DoesNotExist:
        return None

# print (get_books_by_author("jack forest"))
# print(Library.objects.all())
# lib_abrehot = Library.objects.get(name="abrehot")

# print(get_librarian_for_library("abrehot"))


# def books_in_a_lib(library_name):
#     try:
#         all_books = Library.objects.get(name = library_name)
#         return all_books.book_inlab.all() # using realted names
    
#     except Library.DoesNotExist:
#             return None

# # def 