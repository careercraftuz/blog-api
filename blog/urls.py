from django.urls import path
from .views import UserView, Users, CreateUser, PostsView, DeletePostView

urlpatterns = [
    path('users/<int:id>', UserView.as_view()),
    path('users/', Users.as_view()),
    path('users/', CreateUser.as_view()),
    path('posts/', PostsView.as_view()),
    path('delete-post/', DeletePostView.as_view()),
]