from django.contrib import admin
from django.contrib.auth.models import User
from .models import Post

admin.site.register([Post])