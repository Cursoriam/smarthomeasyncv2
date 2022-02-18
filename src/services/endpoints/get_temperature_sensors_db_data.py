import asyncio
from typing import List

from src.sqlite import DBManager
from src.sqlite import TableManager
from src.sqlite import handle_extracted_data


async def get_sensors_data_from_db(sensor_id: str, table_manager: TableManager, db_manager: DBManager) -> List:
    """
    Извлечение данных кондиционера из базы данных
    :param sensor_id:
    :return:
    """

    records = []
    try:
        records = db_manager.execute_single_command(table_manager.extract_command(sensor_id)).fetchall()
    except Exception as err:
        print(err)
    records_data = []
    if len(records):
        records_data = handle_extracted_data(table_manager, records[0])
    return records_data
