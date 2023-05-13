from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User

# Create your views here.
class UserView(APIView):
    def get(self, request: Request, id: int) -> Response:
        try:
            user = User.objects.get(id=id)
            data = {
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name
            }
            return Response(data, status=status.HTTP_200_OK)
        except:
            Response({"Error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)