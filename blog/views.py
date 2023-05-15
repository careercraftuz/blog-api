from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status


from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import Post
from .serializers import PostSerializer


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
        

class PostsView(APIView):
    def get(self, request: Request) -> Response:
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response({"posts": serializer.data})
        

class CreateUser(APIView):
    def post(self,request):
        data=request.data
        username=data.get('username', None)
        password=data.get('password', None)
        first_name=data.get('first_name', None)
        last_name=data.get('last_name', None)
        if username==None or password==None:
            return Response({'result':'didn\'t input required data'})
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

class UpdatePost(APIView):
    def post(self , request:Request)->Response:
            
     
        user = request.user
        try:
                post = Post.objects.filter(user=user).all()
                post = Post.objects.get(id=id)
                try:
                    data = request.data
                    serializer =PostSerializer(post, data=data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                    
                    return Response({'result':serializer.data},status=status.HTTP_200_OK)
                except Exception as e:
                    return Response({'result':f'Bad request {e}'},status=status.HTTP_400_BAD_REQUEST)
                
        except:
                return Response({'result':'Not found task'},status=status.HTTP_404_NOT_FOUND)