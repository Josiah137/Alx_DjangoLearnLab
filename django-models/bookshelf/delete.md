# Delete Operation   

Command: 
#from bookshelf.models import Book  

# Retrieve the book you want to delete  
#book = Book.objects.get(title="1984")  

# Delete the book instance  
#book.delete()  # This will remove the book from the database

#output: (1, {'bookshelf.Book': 1})

# Delete a Book Entry  

This document explains how to delete an existing book entry in the library system.  

### Example Code  

```python  
from bookshelf.models import Book  

# Delete an existing book entry  
book = Book.objects.get(title="Nineteen Eighty-Four")  
book.delete()
