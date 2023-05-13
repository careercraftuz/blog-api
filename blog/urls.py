from django.urls import path
from .views import UserView,CreateUser,Users

urlpatterns = [
    path('users/<int:id>', UserView.as_view()),
    path('userss/',CreateUser.as_view()),
    path('users/',Users.as_view()),
]

