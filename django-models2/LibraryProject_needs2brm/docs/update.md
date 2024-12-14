# Update Operation   

Command:  
```python  
from bookshelf.models import Book  

# Retrieve the book first  
book = Book.objects.get(title="1984")  

# Update the book attributes  
book.author = "George Orwell (Updated)"  
book.publication_year = 1950  
book.save()  # Save the changes
