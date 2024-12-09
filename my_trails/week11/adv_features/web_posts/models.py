from django.db import models

# Create your models here.
class posting(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField()
    image = models.URLField()
    # image = models.ImageField(upload_to=)

    
    
    class Meta:
        permissions = [
            ("can_hide_post", "Can hide post"),
        ]

