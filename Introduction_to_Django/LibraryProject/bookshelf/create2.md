# Create a Book Entry  

This document outlines the process of creating a book entry in our library system using Django's ORM.  

## Usage  

To create a new book entry, you can use the `Book.objects.create` method provided by Django's ORM. This method creates and saves a new instance of the `Book` model in the database. Below is an example of how to use it.  

### Example Code  

```python  
from bookshelf.models import Book  

# Create a new book entry  
new_book = Book.objects.create(  
    title="The Great Gatsby",  
    author="F. Scott Fitzgerald",  
    published_date="1925-04-10",  
    isbn="9780743273565",  
    cover_image="url/to/image.jpg",  
    description="A novel set in the Roaring Twenties, telling the story of Jay Gatsby."  
)  

print(f"Book created: {new_book.title} by {new_book.author}")
