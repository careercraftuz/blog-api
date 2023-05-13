from django.urls import path
from .views import UserView,Users

urlpatterns = [
    path('users/<int:id>', UserView.as_view()),
    path('create/', UserView.as_view()),
]
