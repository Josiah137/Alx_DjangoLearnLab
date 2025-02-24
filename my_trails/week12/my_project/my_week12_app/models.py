from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title, "by", self.author
    
    # if you want to get detail info you can make another func
    def full_info(self):
        return f"{self.title} {self.author} on {self.published_date}"