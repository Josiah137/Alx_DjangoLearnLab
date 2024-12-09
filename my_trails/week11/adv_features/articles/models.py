from django.db import models

# Create your models here.

class JournalArticles(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    written_by = models.CharField(max_length=100)
    written_date = models.DateField()

    def __str__(self):
        return self.title


    class Meta:
        permissions = [
                      ("can_view", "can view articles"), 
                      ("can_create", "can create articles"),
                      ("can_edit", "can edit articles") ,
                      ("can_delete", "can delete articles")
                      ]
