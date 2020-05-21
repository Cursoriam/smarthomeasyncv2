import aiohttp
from aiohttp import web


async def get_lamp_data(request: aiohttp.web.Request) -> aiohttp.web.Response:
    """
    Получение данных от освещения
    :param request:
    :return: aiohttp.web.Response
    """
    response = request.json()
    return web.json_response(response)
