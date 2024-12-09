from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# usually it is imported in this way beacuse i it does not confuse peopel with the calss name. i changed the class name 
# to MyUserAdmin but usually it is UserAdmin (since it is acting as the orginal UserAdmin) and not to confuse it 
# we set the orginal usser admin to BaseuserAdmin
from .models import User

class MyUserAdmin(BaseUserAdmin):
    list_display = ["username", "email", "is_staff", ]
    change_password_form = True
    

admin.site.register(User, MyUserAdmin)


