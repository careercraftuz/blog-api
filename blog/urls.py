from django.urls import path
from .views import (
    UserView,
    Users,
    CreateUser,
    PostsView,
    PostView,
    CreatePostView,
    UpdatePost,
    DeletePostView,
    LoginUser,
    CreateReactionView
)

urlpatterns = [
    path('users/<int:id>', UserView.as_view()),
    path('users/', Users.as_view()),
    path('create-user/', CreateUser.as_view()),
    path('login-user', LoginUser.as_view()),
    path('posts/', PostsView.as_view()),
    path('create-post/', CreatePostView.as_view()),
    path('update/<int:id>', UpdatePost.as_view()),
    path('delete-post/<int:id>', DeletePostView.as_view()),
    path('create-reaction/', CreateReactionView.as_view()),
]
