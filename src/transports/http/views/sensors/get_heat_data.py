import datetime

from aiohttp import web
from aiohttp.web_response import json_response

from src.services.endpoints import get_sensors_data_from_db
from src.sqlite import heat_table_manager
from src.sqlite import sensors_data_db_manager


async def get_heat_data(request: web.Request) -> web.Response:
    """
    Получение данных потребления теплоты
    :param request:
    :return: web.Response
    """
    sensor_id = request.query.get('sensor_id')
    heat_sensors_data = [0.4, 0.2, 0.3, 0.3, 0.6, 0, 0, 0, 0, 0, 0.9]
    heat_sensors_data = [{'date_n_time': str(datetime.datetime.now()), 'sensor_id': 1, 'Quantity': sensor_data}
                         for sensor_data in heat_sensors_data]
    heat_sensors_data_from_db = await get_sensors_data_from_db(sensor_id, heat_table_manager, sensors_data_db_manager,
                                                               -1)
    heat_sensors_data.append(heat_sensors_data_from_db[-1])
    return json_response(data=heat_sensors_data)
