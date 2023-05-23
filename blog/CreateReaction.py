from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class CreateReaction(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Get the input data from the request
        user = request.data.get('user')
        post = request.data.get('post')
        like = request.data.get('like', False)

        # Perform the necessary actions to create the reaction
        # (e.g., save the reaction in the database)

        # Return the response
        response_data = {"message": "Reaction created successfully."}
        return Response(response_data, status=201)
