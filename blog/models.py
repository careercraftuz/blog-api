from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length=75)
    content = models.TextField()
    publication_date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, related_name=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title

