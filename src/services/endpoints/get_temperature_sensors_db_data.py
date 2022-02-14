import asyncio
from typing import List

from src.sqlite import execute_single_command
from src.sqlite import TableManager
from src.sqlite import handle_extracted_data


async def get_sensors_data_from_db(sensor_id: str, table_manager: TableManager) -> List:
    """
    Извлечение данных кондиционера из базы данных
    :param sensor_id:
    :return:
    """

    count = execute_single_command(table_manager.create_extract_all_command())
    if not count.fetchall():
        await asyncio.sleep(10)

    records = execute_single_command(table_manager.extract_command(sensor_id)).fetchall()
    records_data = handle_extracted_data(table_manager, records)
    return records_data
