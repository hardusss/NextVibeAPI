from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers_pac import UserRegistrationSerializer


class RegisterUserView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            user_data = UserRegistrationSerializer(user, context={'request': request}).data
            return Response(
                {
                    "message": "User registered successfully.",
                    "user_id": user.user_id,  
                    "data": user_data,
                },
                status=status.HTTP_201_CREATED
            ) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)