import time

import aiohttp
from aiohttp import web

from services.endpoints import get_conditioner_status_data


async def get_conditioner_status(request):
    records = await get_conditioner_status_data(request)

    return web.Response(text='hello')

