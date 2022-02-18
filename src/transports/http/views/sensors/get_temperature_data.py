from aiohttp import web

from src.services.endpoints import get_sensors_data_from_db
from src.sqlite import temperature_table_manager
from src.sqlite import db_manager


async def get_temperature_data(request: web.Request) -> web.Response:
    """
    Получение данных кондиционера
    :param request:
    :return: web.Response
    """
    sensor_id = request.query.get('sensor_id')
    temperature_sensors_data = await get_sensors_data_from_db(sensor_id, temperature_table_manager, db_manager)
    return web.json_response(temperature_sensors_data)
