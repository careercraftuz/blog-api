from django.contrib import admin
from .models import Post, Reaction
# Register your models here.
admin.site.register([Post, Reaction])