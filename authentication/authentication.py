import jwt
import datetime
from django.conf import settings
from authentication.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication(BaseAuthentication):
    """
    Custom authentication class for handling JWT tokens.
    """

    def __init__(self):
        self.secret_key = settings.SECRET_KEY  # Ensure secret key is initialized correctly

    def generate_jwt_token(self, user_id):
        """
        Generates a JWT token for a given user_id.
        """
        payload = {
            'user_id': user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),  # Token expires in 24 hours
            'iat': datetime.datetime.utcnow()  # Issued at
        }
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token

    def decode_jwt_token(self, token):
        """
        Decodes a JWT token.
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')

    def authenticate(self, request):
        """
        Authenticates the request using the JWT token.
        """
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        try:
            prefix, token = auth_header.split(' ')
            if prefix.lower() != 'bearer':
                raise AuthenticationFailed('Invalid token prefix')
        except ValueError:
            raise AuthenticationFailed('Invalid token header')

        payload = self.decode_jwt_token(token)
        user_id = payload['user_id']

        try:
            user = User.objects.get(id=user_id)  # Adjust this to use your custom User model if needed
        except User.DoesNotExist:
            raise AuthenticationFailed('User not found')

        return (user, token)