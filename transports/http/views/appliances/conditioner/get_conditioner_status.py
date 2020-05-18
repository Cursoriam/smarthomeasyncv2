import aiohttp
from aiohttp import web

from services.endpoints import get_conditioner_status_data


async def get_conditioner_status(request: aiohttp.web.Request) -> aiohttp.web.Response:
    # records = await get_conditioner_status_data(request)
    try:
        return web.Response(text='hello')
    except Exception as ex:
        raise ex
