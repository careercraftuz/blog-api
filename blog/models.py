from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title   = models.CharField(max_length=255)
    content = models.TextField()
    publication_data = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title