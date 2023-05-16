from django.urls import path
from .views import (
    UserView,
    Users,
    CreateUser,
    PostsView,
    PostView,
    CreatePostView,
    UpdatePost,
    DeletePostView
    )

urlpatterns = [
    path('users/<int:id>', UserView.as_view()),
    path('users/', Users.as_view()),
    path('users/', CreateUser.as_view()),
    path('posts/', PostsView.as_view()),
    path('create-post/',CreatePostView.as_view()),
    path('update/<int:id>',UpdatePost.as_view()),
    path('delete-post/<int:id>',DeletePostView.as_view),
    path('posts/<int:id>', PostView.as_view()),
]