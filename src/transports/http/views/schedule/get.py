from aiohttp import web
from src.services.endpoints import get_recuperator_schedule_from_db


async def get_recuperator_schedule(request: web.Request):
    """
    Обновление расписания рекуператора
    @param request:
    """
    records = await get_recuperator_schedule_from_db(request)

    return web.json_response(records)
