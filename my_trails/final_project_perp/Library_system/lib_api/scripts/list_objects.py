import os
import django
import sys

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Library_system.settings')
django.setup()

from django.contrib.auth.models import User
from lib_api.models import Book, Author, Genre  # Replace with your actual app and model names

def list_users():
    print("=== Users ===")
    users = User.objects.all()
    for user in users:
        print(f"Username: {user.username}, Email: {user.email}, Is Staff: {user.is_staff}")

def list_books():
    print("\n=== Books ===")
    books = Book.objects.all()
    for book in books:
        # print(f"Title: {book.title}, Author: {book.author}, Genre: {', '.join([genre.name for genre in book.genre.all()])}")
        print(f"Title: {book.name},\n\t Author: {book.author},\n\t Genre: {', '.join([genre.name for genre in book.genre.all()])}")

def list_authors():
    print("\n=== Authors ===")
    authors = Author.objects.all()
    for author in authors:
        print(f"Name: {author.name}")  # Replace 'name' and 'bio' with your model's fields

def list_genres():
    print("\n=== Genres ===")
    genres = Genre.objects.all()
    for genre in genres:
        print(f"Name: {genre.name}")  # Replace 'name' with your model's field for genre name

if __name__ == "__main__":
    list_users()
    list_authors()
    list_genres()
    list_books()
