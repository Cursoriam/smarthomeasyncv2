import time

import aiohttp
from aiohttp import web

from services.endpoints import get_conditioner_status_data


async def get_conditioner_status(request) -> aiohttp.web.Response:
    records = await get_conditioner_status_data(request)
    try:
        time.sleep(3)
        return web.Response(text='hello')
    except Exception as ex:
        raise ex
