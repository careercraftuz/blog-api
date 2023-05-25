from django.urls import path
from .views import (
    UserView,
    Users,
    CreateUser,
    PostsView,
    PostView,
    CreatePost,
    UpdatePost,
    DeletePostView,
    LoginUser,
    LogoutUser,
    CreateReaction,
    )


urlpatterns = [
    path('users/<int:id>', UserView.as_view()),
    path('users/', Users.as_view()),
    path('create-user/', CreateUser.as_view()),
    path('login-user', LoginUser.as_view()),
    path('logout-user', LogoutUser.as_view()),
    path('posts/', PostsView.as_view()),
    path('create-post/', CreatePost.as_view()),
    path('update/<int:id>', UpdatePost.as_view()),
    path('delete-post/<int:id>', DeletePostView.as_view()),
    path('posts/<int:id>', PostView.as_view()),
    path('create-reaction', CreateReaction.as_view()),
]