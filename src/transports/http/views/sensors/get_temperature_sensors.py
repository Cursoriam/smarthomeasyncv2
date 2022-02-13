from aiohttp import web

from src.services.endpoints import get_temperature_sensors_status_data


async def get_temperature_sensors(request: web.Request) -> web.Response:
    """
    Получение данных кондиционера
    :param request:
    :return: web.Response
    """
    conditioner_id = request.query.get('id')
    records = await get_temperature_sensors_status_data(conditioner_id)
    records_data = {'id': records[0][1],
                    'status': records[0][3],
                    'temperature': records[0][4],
                    'mode': records[0][5], }  # TODO: Изменить способ генерации
    return web.json_response(records_data)
