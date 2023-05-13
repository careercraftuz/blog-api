from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.request import Request
from rest_framework.response import Response

class UserView(APIView):
    def get(self,request:Request,id:int):
        try:
            user=User.objects.get(id=id)
            return Response({ "username": user.username, "first_name": user.first_name, "last_name": user.first_name})
        except:
            return Response({'result':'User not found'})
    # create user
    def post(self,request:Request):
        data=request.data
        user=User.objects.create_user(username=data['username'],password=data['password'])
        user.save()
        
        return Response({'result':user.username})

