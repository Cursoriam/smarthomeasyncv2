from aiohttp import web
from aiohttp.web_response import json_response

from src.services.endpoints import get_sensors_data_from_db
from src.sqlite import humidity_table_manager
from src.sqlite import db_manager


async def get_humidity_data(request: web.Request) -> web.Response:
    """
    Получение данных кондиционера
    :param request:
    :return: web.Response
    """
    sensor_id = request.query.get('sensor_id')
    humidity_sensors_data = await get_sensors_data_from_db(sensor_id, humidity_table_manager, db_manager, 1)
    return json_response(data=humidity_sensors_data)
