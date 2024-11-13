from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length = 200) 
    puplication_year = models.DateField()
    
    def __str__(self):
        return (f"the book title is: '{self.title}' by {self.author} on {self.puplication_year}")
    # def __str__(self):  
    #     return self.title



