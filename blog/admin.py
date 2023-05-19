from django.contrib import admin
from .models import Post, Reaction


admin.site.register([
    Post,
    Reaction,
])
