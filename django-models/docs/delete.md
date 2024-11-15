# Delete Operation   

Command:  
```python  
from bookshelf.models import Book  

# Retrieve the book you want to delete  
book = Book.objects.get(title="1984")  

# Delete the book instance  
book.delete()  # This will remove the book from the database

#output: (1, {'bookshelf.Book': 1})
