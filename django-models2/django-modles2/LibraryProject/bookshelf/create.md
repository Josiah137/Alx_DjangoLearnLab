# Create a Book Entry  

This document explains how to create a new book entry in the library system.  

### Example Code  

```python  
from bookshelf.models import Book  

# Create a new book entry using Book.objects.create  
new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
