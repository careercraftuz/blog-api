from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth.hashers import make_password
from rest_framework import status

class UserView(APIView):
    def get(self,request,id:int):
        try:
            user=User.objects.get(id=id)
            return Response({
                "username": user.username,
                "first_name": user.first_name, 
                "last_name": user.first_name
            })
        except:
            return Response({'result':'User not found'})
class Users(APIView):
    def get(self,request: Request):
        try:
            data=[]
            users=User.objects.all()
            for user in users:
                data.append({
                    "username": user.username,
                    "first_name": user.first_name,
                    "last_name": user.first_name
                })
            return Response(data)
        except:
            return Response({'result':'Users not found'})

class CreateUser(APIView):
    def post(self,request):
        data=request.data
        username=data.get('username',None)
        password=data.get('password',None)
        first_name=data.get('first_name',None)
        last_name=data.get('last_name',None)
        if username==None or password==None:
            return Response({'result':'username and password are required'})
        try:
            user=User.objects.get(username=username)
            return Response({'result':'Invalid username'})
        except:
            user=User.objects.create(
                username=username,
                password=make_password(password),
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            return Response({ "message": "User created successfully." },status=status.HTTP_201_CREATED)