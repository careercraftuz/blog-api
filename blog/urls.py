from django.urls import path
from .views import UserView,Users,CreateUser

urlpatterns = [
    path('users/<int:id>', UserView.as_view()),
    path('users/',Users.as_view()),
    path('users/',CreateUser.as_view()),
    
]
