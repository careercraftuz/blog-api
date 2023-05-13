from django.urls import path
from .views import UserView,CreateUser

urlpatterns = [
    path('users/<int:id>', UserView.as_view()),
    path('users/',CreateUser.as_view())
]