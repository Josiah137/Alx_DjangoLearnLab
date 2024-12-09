from django.db import models

# Create your models here.
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields): #
        if not email:
            raise ValueError("The Email field must be set")
        # email = self.normalize_email(email)
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return "super user is successfully created!!", user
    # dont forget to link the user manager with the model
    


from django.contrib.auth.models import AbstractUser

#changing the login method to the email and password instad of user name 
class User(AbstractUser):
    email = models.EmailField(unique= True, max_length=150)
    username = models.CharField(max_length=50, unique=False, blank=True, null=True)
 

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager() # inserted to link our user manager and the model. we are specifiying how the object will be created

    def __str__(self):
        return self.email
    
