from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
# from .models import User
from authentication.models import User
from .serializers import UserSerializer
from .authentication import CustomAuthentication

class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Generate a token for the new user
            auth = CustomAuthentication()
            token = auth.generate_jwt_token(user.id)
            return Response({'user': serializer.data, 'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = get_object_or_404(User, email=request.data['email'])
        if user.check_password(request.data['password']):
            auth = CustomAuthentication()  # Use the custom authentication class
            token = auth.generate_jwt_token(user.id)
            return Response({'access': token, 'user_id': user.id}, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        # The `request.user` will be set by the custom authentication class if the user is authenticated
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




















# class SignUpView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         user = get_object_or_404(User, email=request.data['email'])
#         if user.check_password(request.data['password']):
#             refresh = RefreshToken.for_user(user)
#             return Response({'access': str(refresh.access_token),'user_id': user.id}, status=status.HTTP_200_OK)
#         return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

# class UserDetailView(APIView):
#     authentication_classes = [CustomAuthentication]
#     permission_classes = [IsAuthenticated]
    
#     def get(self, request):
#         # Fetch the authenticated user from the custom user model
#         user = request.user  
#         if not isinstance(user, User):  # Ensure the user is from the correct custom model
#             return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#     def put(self, request):
#         # Fetch the authenticated user from the custom user model
#         user = request.user  
#         if not isinstance(user, User):  # Ensure the user is from the correct custom model
#             return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

#         serializer = UserSerializer(user, data=request.data)  # Update user data
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 