from aiohttp import web
from src.services.endpoints import add_or_update_recuperator_schedule


async def change_recuperator_schedule(request: web.Request):
    """
    Обновление расписания рекуператора
    @param request:
    """
    await add_or_update_recuperator_schedule(request)

    return web.json_response(data="Schedule successfully changed")
