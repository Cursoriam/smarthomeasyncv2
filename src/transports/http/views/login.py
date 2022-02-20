from datetime import datetime
from datetime import timedelta

from aiohttp import web
from aiohttp.web_response import json_response
import jwt

from src.constants import JWT_SECRET
from src.constants import JWT_ALGORITHM
from src.constants import JWT_EXP_DELTA_MINUTES
from src.models import User


async def login(request: web.Request) -> web.Response:
    post_data = await request.json()
    try:
        user = User.objects.get(email=post_data['email'])
        # user.match_password(post_data['password']+JWT_SECRET)
    except (User.DoesNotExist, User.PasswordDoesNotMatch):
        return json_response({'message': 'Wrong credentials'}, status=400)

    payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(minutes=JWT_EXP_DELTA_MINUTES)
    }

    jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return json_response({'token': jwt_token})
