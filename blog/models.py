from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title[:20]}... by {self.author.username} at {self.created_at.day}/{self.created_at.month}/{self.created_at.year}'
    


class Reaction(models.Model):
    like = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        if self.like:
            return f'{self.user.username} liked {self.post.title[:20]}... at {self.post.created_at.day}/{self.post.created_at.month}/{self.post.created_at.year}'
        return f'{self.user.username} disliked {self.post.title[:20]}... at {self.post.created_at.day}/{self.post.created_at.month}/{self.post.created_at.year}'
