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