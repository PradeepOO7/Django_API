import re
import jwt
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken
from Advisor_Network.settings import SIMPLE_JWT
def get_tokens_for_user(user):
    refresh = AccessToken.for_user(user)
    return str(refresh)
    
def isAuthenticated(request,uid):
    try:
        JWT_authenticator = JWTAuthentication()
        response = JWT_authenticator.get_header(request)
        st=str(JWT_authenticator.get_raw_token(response))
        data=jwt.decode(st[2:-1],SIMPLE_JWT['SIGNING_KEY'],algorithms=SIMPLE_JWT['ALGORITHM'])
        if data["user_id"]==uid:
            return True
        else:
            return False
    except Exception :
        return "Exception"