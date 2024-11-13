from django.contrib import admin

# Register your models here.

from .models import Books

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'puplication_year')
    search_fields = ('title', 'author')

admin.site.register(Books, BookAdmin)


#     list_display = ('ti')
# admin.site.register(Books)
