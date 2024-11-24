from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render  
from .models import Book  # Make sure to import your Book model  

def list_books(request):  
    books = Book.objects.all()  # Retrieve all books from the database  
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Render the template with books


from django.views.generic.detail import DetailView  
from .models import Library  # Import your Library model  

class LibraryDetailView(DetailView):  
    model = Library  # Specify the model to use  
    template_name = 'relationship_app/library_detail.html'  # Specify the template to render  
    context_object_name = 'library'  # Name of the context object to use in the template  

    def get_queryset(self):  
        return Library.objects.prefetch_related('books')  # Prefetch related books for efficiency
    


# from django.contrib.auth import login, logout, authenticate  
# from django.contrib.auth.forms import UserCreationForm  
# from django.shortcuts import redirect # importing along with rendering

# relationship_app/views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login


# Custom registration view
def register(request):
    if request.method == "POST": # This typically means the user has filled the registration form and click submit.
        form = UserCreationForm(request.POST) #This line creates an instance of UserCreationForm
        if form.is_valid(): # This checks if the submitted data meets all validation criteria defined in the UserCreationForm.
            user = form.save() # The user is created in the database using the valid data.
            login(request, user)  # Log in the user after registration
            return redirect("home")  # Redirect to a 'home' page after successful registration
    else:
        form = UserCreationForm() # means GET method gives an empty form to user to be filled (see ur not on excersie for more info)
    return render(request, "relationship_app/register.html", {"form": form})


def home(request):
    return render(request, "relationship_app/home.html")





# below is to set up role based views

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from .models import UserProfile

# Check if the user is an Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Check if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Check if the user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view, accessible only by users with the 'Admin' role
# @user_passes_test(is_admin)
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')


from django.contrib.auth.decorators import login_required
@login_required
@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


# Librarian view, accessible only by users with the 'Librarian' role
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view, accessible only by users with the 'Member' role
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
