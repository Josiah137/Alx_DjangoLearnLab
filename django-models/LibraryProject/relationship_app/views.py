from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render  
from .models import Book  # Make sure to import your Book model  

def list_books(request):  
    books = Book.objects.all()  # Retrieve all books from the database  
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Render the template with books


from django.views.generic import DetailView  
from .models import Library  # Import your Library model  

class LibraryDetailView(DetailView):  
    model = Library  # Specify the model to use  
    template_name = 'relationship_app/library_detail.html'  # Specify the template to render  
    context_object_name = 'library'  # Name of the context object to use in the template  

    def get_queryset(self):  
        return Library.objects.prefetch_related('books')  # Prefetch related books for efficiency
    


from django.contrib.auth import login, logout, authenticate  
from django.contrib.auth.forms import UserCreationForm  
from django.shortcuts import redirect # importing along with rendering