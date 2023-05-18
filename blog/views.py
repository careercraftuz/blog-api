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
            return Response({'result':'User ID not found'})
        

class Users(APIView):
    def get(self,request):
        try:
            data=[]
            users=User.objects.all()
            for user in users:
                data.append({ "username": user.username, "first_name": user.first_name, "last_name": user.first_name})
            return Response(data)
        except:
            return Response({'result':'No users list found'})
        

class PostsView(APIView):
    def get(self, request: Request) -> Response:
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response({"posts": serializer.data})
    

class PostView(APIView):
    def get(self, request: Request, id: int) -> Response:
        try:
            post = Post.objects.get(id=id)
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"Status": "This post doesn't exist."}, status=status.HTTP_404_NOT_FOUND)
        

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


class CreatePostView(APIView):
    def post(self,request:Request):
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=401)


class UpdatePost(APIView):
    def put(self,request:Request,id:id)->Response:
        user = request.user
        try:
            task = Post.objects.get(user=user,id=id)
            data = request.data
            serializer = PostSerializer(task, data=data, partial=True)
            if serializer.is_valid():
                 serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
                return Response({'result':'Not found task'},status=status.HTTP_404_NOT_FOUND)

class DeletePostView(APIView):
    def post(self,request,id:int):
        try:
            post=Post.objects.get(id=id)
            post.delete()
            return Response(
                { "status": "deleted post"},
                status=status.HTTP_200_OK
            )
        except:
            return Response({'status':'Post Not Found'}, status=status.HTTP_404_NOT_FOUND)

