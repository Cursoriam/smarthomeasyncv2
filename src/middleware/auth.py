from typing import Optional

from aiohttp import web
from aiohttp.web_response import json_response
import jwt

from src.constants import JWT_SECRET
from src.constants import JWT_ALGORITHM
from src.models import User


async def get_user(request):
    return json_response({'user': str(request.user)})


async def auth_middleware(app, handler):
    async def middleware(request):
        request.user = None
        jwt_token = request.headers.get('authorization', None)
        if jwt_token:
            try:
                payload = jwt.decode(jwt_token, JWT_SECRET,
                                     algorithms=[JWT_ALGORITHM])
            except (jwt.DecodeError, jwt.ExpiredSignatureError):
                return json_response({'message': 'Token is invalid'}, status=400)

            request.user = User.objects.get(id=payload['user_id'])
        return await handler(request)
    return middleware


