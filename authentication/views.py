from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.urls import reverse 
from django.core.mail import send_mail
# from .models import User
from authentication.models import User
from .serializers import UserSerializer, UserUpdateSerializer
from .authentication import CustomAuthentication
import logging

logger = logging.getLogger(__name__)

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
            return Response({'token': token, 'user_id': user.id}, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # The `request.user` will be set by the custom authentication class
        if request.user:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        else:
            return Response({"error": "User not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request):
        if request.user:
            serializer = UserUpdateSerializer(request.user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "User not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)


class ForgotPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        if not email:
            return Response({"error": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = get_object_or_404(User, email=email)
            logger.info(f"Processing password reset for email: {email}")

            # Generate reset token
            auth = CustomAuthentication()
            reset_token = auth.generate_reset_token(user)

            # Generate reset link
            reset_url = request.build_absolute_uri(reverse("reset-password", args=[reset_token]))
            logger.info(f"Generated reset URL: {reset_url}")

            print("--------------------------------------", reset_url)
            # Send email with reset link
            send_mail(
                subject="Password Reset Request",
                message=f"Click the link below to reset your password:\n{reset_url}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
            )

            return Response(
                {"message": "Password reset link sent to your email."},
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            logger.error(f"Error processing forgot password request: {e}")
            return Response(
                {"error": "An error occurred while processing your request."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

class ResetPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, token):
        new_password = request.data.get("password")
        user = get_object_or_404(User, reset_token=token)

        # Reset the user's password
        user.set_password(new_password)
        user.reset_token = ""  # Clear the reset token after use
        user.save()

        return Response({"message": "Password reset successful."}, status=status.HTTP_200_OK)

