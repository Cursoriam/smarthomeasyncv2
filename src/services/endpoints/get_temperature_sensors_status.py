# TODO:
import asyncio
from typing import List

import sqlite3


async def get_temperature_sensors_status_data(conditioner_id: str) -> List:
    """
    Извлечение данных кондиционера из базы данных
    :param conditioner_id:
    :return:
    """
    sqlite_connection = sqlite3.connect('SmartHome.db')
    cursor = sqlite_connection.cursor()

    count = "SELECT * FROM CONDITIONER_DATA"
    count_of_values = cursor.execute(count)
    if not count_of_values.fetchall():
        await asyncio.sleep(10)

    cursor.execute('SELECT name from sqlite_master where type= "table"')

    sqlite_select_query = (
        """SELECT * from CONDITIONER_DATA WHERE ConditionerID=""" + conditioner_id
        + """ ORDER BY Date_n_Time DESC LIMIT 1"""
    )
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    return records
