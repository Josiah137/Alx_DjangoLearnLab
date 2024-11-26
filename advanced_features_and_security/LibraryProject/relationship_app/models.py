from django.db import models

# i Create my models here.

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    # additional feature just to enhace it by ensuring there is no dupllicate    
    class Meta:
        unique_together = ('title', 'author')  # Enforces unique titles per author

    def __str__(self):
        return f"{self.title} by {self.author.name}"

class Library(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, related_name="libraries")

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, null= True, blank=True, related_name="librarians") # the null= True, blank=True are not nessasry for this to work.
    # unless the field is many to many, by default we need to fill every attribute of a class when we create an instance. to by pass that you can add those methods. ex:
    # ex: let say diffrent librarian registerd for the position but you haven't decided which librarian goes to which library yet. 
    # you register the names alone and then later on you can add their respective library. (if u want to can trun this off later on and update your modle to not all such methods after the data is filled up)
    
    def __str__(self):
        # return f"{self.name} working in {self.library.name}"
        # it was like what i commented above but it throw error for the librarians who have no library since we are trying to return that 
        # (since i want librarians with no library exist i set additional feature)
        
        if self.library:
            return f"{self.name} working in {self.library.name}"
        return f"{self.name} with no associated library" #This ensures that the method doesn’t break if library is None.
        
# you can test it in the shell. with what i have alrady created




from django.contrib.auth.models import User

# Extend the User model with a one-to-one relationship to store additional profile information
class UserProfile(models.Model):
    # Choices for user roles
    ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

  

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Django signals to automatically create and update the user profile when a user is created or updated
# the explaintion  is on GPT in detail(name = debugging dgango on eyos73)


from django.db.models.signals import post_save
from django.dispatch import receiver
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a UserProfile when a new user is created
        UserProfile.objects.create(user=instance, role='Member')  # Default role
    # Update the profile if user already exists (optional, might be unnecessary here)
    instance.userprofile.save()




       
    
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

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
    profile_photo = models.ImageField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    #linking the objects created with the user manager
    # objects = UserManger()

    def __str__(self):
        return self.email
       
       


