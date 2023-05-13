from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User

class UserView(APIView):
    def get(self,request:Request,pk):
        user = User.objects.get(id=pk)
        data =[{
            "username":user.username,
            "first_name":user.first_name,
            "last_name":user.last_name
         }]
        return Response(data)