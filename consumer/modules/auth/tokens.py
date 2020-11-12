import jwt
from django.conf import settings

def genToken(payload):
    token= jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    return token