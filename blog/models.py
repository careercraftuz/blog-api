from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title   = models.CharField(max_length=255)
    context = models.TextField(max_length=50)
    publication_data = models.DateTimeField(auto_created=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title