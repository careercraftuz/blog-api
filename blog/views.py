from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import Post
from .serializers import PostSerializer, ReactionSerializer


class UserView(APIView):
    def get(self, request, id: int):
        try:
            user = User.objects.get(id=id)
            return Response({"username": user.username, "first_name": user.first_name, "last_name": user.first_name})
        except:
            return Response({'result': 'The User you searched for was not found'})


class Users(APIView):
    def get(self, request):
        try:
            data = []
            users = User.objects.all()
            for user in users:
                data.append({"username": user.username,
                            "first_name": user.first_name, "last_name": user.first_name})
            return Response(data)
        except:
            return Response({'result': 'Users not found'})


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
    def post(self, request: Request) -> Response:
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        if username == None or password == None:
            return Response({'result': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(username=username)
            return Response({'result': 'This user already exists'})
        except:
            user = User.objects.create(
                username=username,
                password=make_password(password)
            )
            user.save()
            token = Token.objects.create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)


class CreatePost(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request: Request):
        data = request.data
        data["author"] = request.user.id
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
          
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)



class UpdatePost(APIView):
    def put(self, request: Request, id: id) -> Response:
        user = request.user
        try:
            task = Post.objects.get(user=user, id=id)
            data = request.data
            serializer = PostSerializer(task, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'result': 'Not found task'}, status=status.HTTP_404_NOT_FOUND)


class DeletePostView(APIView):
    def post(self, request, id: int):
        try:
            post = Post.objects.get(id=id)
            post.delete()
            return Response(
                {"status": "deleted post"},
                status=status.HTTP_200_OK
            )
        except:
            return Response({'status': 'Post Not Found'}, status=status.HTTP_404_NOT_FOUND)


class LoginUser(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request: Request) -> Response:
        user = request.user
        token = Token.objects.filter(user=user)
        if len(token) > 0:
            token.delete()
        token = Token.objects.create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)
    

class LogoutUser(APIView):
    authentication_classes=[TokenAuthentication]
    
    def post(self, request:Request)->Response:
        user= request.user
        try:
            token = Token.objects.get(user=user)
            token.delete()
            return Response({"result":"user logout "}, status=status.HTTP_200_OK)
          
        except:
            return Response({'result': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        

class CreateReaction(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request: Request) -> Response:
        data = request.data
        data['user'] = request.user.id
        serializer = ReactionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Reaction created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
