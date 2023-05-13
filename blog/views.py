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
        

class Users(APIView):
    def get(self,request):
        try:
            data=[]
            users=User.objects.all()
            for user in users:
                data.append({ "username": user.username, "first_name": user.first_name, "last_name": user.first_name})
            return Response(data)
        except:
            return Response({'result':'Users not found'})


class CreateUser(APIView):
    def post(self, request: Request) -> Response:
        data = request.data
        username = data.get('username')
        password = data.get('username')
        user = User.objects.filter(username=username, password=password)
        if len(user):
            return Response({"message": "User already exist."})
        else:
            user = User.objects.create(
                username = username,
                password = password,
                first_name = data.get('first_name', ''),
                last_name = data.get('last_name', '')
            )
            return Response({"message": "User created successfully."})
