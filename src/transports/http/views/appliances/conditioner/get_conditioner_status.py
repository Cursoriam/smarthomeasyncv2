from aiohttp import web

from src.services.endpoints import get_conditioner_status_data


async def get_conditioner_status(request: web.Request) -> web.Response:
    """
    Получение данных кондиционера
    :param request:
    :return: web.Response
    """
    conditioner_id = request.query.get('id')
    records = await get_conditioner_status_data(conditioner_id)
    records_data = {'id': records[0][1], 'status': records[0][3], 'temperature': records[0][4], 'mode': records[0][5]}
    return web.json_response(records_data)
