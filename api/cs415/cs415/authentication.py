from datetime import datetime, timedelta
import jwt
from cs415.models import User
from django.conf import settings
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed, ParseError


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # Extract the JWT from the Authorization header
        jwt_token = request.META.get("HTTP_AUTHORIZATION")
        # print(jwt_token)
        if jwt_token is None:
            return None

        jwt_token = JWTAuthentication.get_the_token_from_header(
            jwt_token
        )  # clean the token
        # Decode the JWT and verify its signature
        try:
            payload = jwt.decode(jwt_token, key="valhalla", algorithms=["HS256"])
        except jwt.exceptions.InvalidSignatureError:
            raise AuthenticationFailed("Invalid signature")
        except jwt.exceptions.ExpiredSignatureError:
            raise AuthenticationFailed("Expired signature")
        except Exception as err:
            print(err)
            raise ParseError()

        # Return the token payload
        return payload

    def authenticate_header(self, request):
        return "Bearer"

    @classmethod
    def create_jwt(cls, user):
        # Create the JWT payload
        payload = {
            "user_id": user.user_id,
            "scope": "admin",
            "first_name": user.first_name,
            "last_name": user.last_name,
            "exp": datetime.utcnow() + timedelta(hours=8),
            "iat": datetime.utcnow(),
        }

        # Encode the JWT with your secret key
        jwt_token = jwt.encode(payload, key="valhalla", algorithm="HS256")

        return jwt_token

    @classmethod
    def get_the_token_from_header(cls, token):
        token = token.replace("Bearer", "").replace(" ", "")  # clean the token
        return token
