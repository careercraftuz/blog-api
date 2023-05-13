from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    tasks = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'tasks')