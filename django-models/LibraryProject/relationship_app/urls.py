from django.urls import path  
from .views import list_books, LibraryDetailView  

from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [  
    path('books/', list_books, name='list_books'),  # URL for the function-based view  
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for the class-based view  
    
    # Registration URL
    path("register/", views.register, name="register"),
    
    # Login URL
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    
    # Logout URL
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),

    path("", views.home, name="home"),  # Home page URL
]