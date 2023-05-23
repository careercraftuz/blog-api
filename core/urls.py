from django.contrib import admin
from django.urls import path, include
from .CreateReaction import CreateReaction


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
    path('api/create-reaction', CreateReaction.as_view(), name='create-reaction'),
]
