from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.request import Request

class UserView(APIView):
    def get(self,request,id:int):
        try:
            user=User.objects.get(id=id)
            return Response({ "username": user.username, "first_name": user.first_name, "last_name": user.first_name})
        except:
            return Response({'result':'User not found'})
class CreateUser(APIView):
    def post(self,request:Request):
        data=request.data
        username= data.get('username',False)
        password = data.get('password',False)
        first_name = data.get('first_name',False)
        last_name = data.get('last_name',False)
        user = User.objects.filter(username=username,password=password)
        if not user:
            user = User.objects.create(username=username,password=password,first_name=first_name,last_name=last_name)
            return Response({ "message": "User created successfully." })
        else:
            return Response({"result":"such a user exists"})