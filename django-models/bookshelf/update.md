# Update a Book Entry  

This document explains how to update an existing book entry in the library system.  

### Example Code  

```python  
from bookshelf.models import Book  

# Update an existing book entry  
book = Book.objects.get(title="1984")  
book.title = "Nineteen Eighty-Four"  
book.save()
