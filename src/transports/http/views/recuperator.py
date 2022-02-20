from aiohttp import web
from aiohttp.web_response import json_response
from src.utils import access_token_required
from src.publishers import publish_recuperator_data


@access_token_required
async def change_recuperator_mode(request: web.Request):
    post_data = await request.json()
    publish_recuperator_data(post_data["mode"])
    return json_response({'message': 'Mode changed'})
