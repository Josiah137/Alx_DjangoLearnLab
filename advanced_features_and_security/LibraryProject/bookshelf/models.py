from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManger(BaseUserManager):
    def Create_user(self, email, passwd=None, **additional_fileds):
        if not email:
            raise ValueError("please provide correct email")
        if not passwd:
            raise ValueError("please provide the right password")
        
        newuser = self.model(email = self.normalize_email(email), **additional_fileds)
        newuser.set_password(passwd)
        newuser.save(using=self._db)
        return newuser
    
    def Create_superuser(self, email, passwd=None, **additional_fileds):
        newuser = self.Create_user(email, passwd, additional_fileds)

        newuser.is_staff = True
        newuser.is_superuser = True

        newuser.save(using=self._db)
        return newuser
            

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=150)
    username = models.CharField(unique=False, max_length=50, blank=True, null=True)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to="profile_pictures/")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    #linking the objects created with the user manager
    # objects = UserManger()

    def __str__(self):
        return self.email
       
       


