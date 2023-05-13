from django.urls import path
from .views import UserView, Users, PostsView

urlpatterns = [
    path('users/<int:id>', UserView.as_view()),
    path('users/',Users.as_view()),
    path('api/posts/', PostsView.as_view())
]
