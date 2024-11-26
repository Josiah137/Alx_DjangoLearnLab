from django.contrib import admin

# Register your models here. 
from .models import Book  

# Register the Book model with the admin  
# admin.site.register(Book)


class BookAdmin(admin.ModelAdmin):  
    # Specify the fields to display in the list view  
    list_display = ('title', 'author', 'publication_year')  
    
    # Add filters for publication year  
    list_filter = ('publication_year',)  
    
    # Enable search functionality on title and author  
    search_fields = ('title', 'author__name')  

# Register the Book model with the custom admin class  
admin.site.register(Book, BookAdmin)


from .models import CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class MyUserAdmin(BaseUserAdmin):
    list_display = ["email", "is_staff"]

admin.site.register(CustomUser, MyUserAdmin)