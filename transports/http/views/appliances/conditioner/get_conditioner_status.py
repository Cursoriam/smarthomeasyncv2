from aiohttp import web

from services.endpoints import get_conditioner_status_data


async def get_conditioner_status(request: web.Request) -> web.Response:
    id = request.query.get('id')
    records = await get_conditioner_status_data(id)
    return web.json_response(records)

