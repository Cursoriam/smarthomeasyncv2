import json
import sqlite3
from typing import List
from typing import Tuple
from typing import Union

# SQLite DB Name
DB_NAME = 'SmartHome.db'


# ===============================================================
# Database Manager Class


class DatabaseManager:
    """
    Менеджер для управления базой данных
    """
    def __init__(self) -> None:
        self.conn = sqlite3.connect(DB_NAME)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def add_del_update_db_record(self, sql_query: str, args: Union[List, Tuple] = ()) -> None:
        """
        Метод для добавления изменений или удаления из базы данных
        :param sql_query:
        :param args:
        :return:
        """
        self.cur.execute(sql_query, args)
        self.conn.commit()

    def __del__(self) -> None:
        self.cur.close()
        self.conn.close()


# ===============================================================
# Functions to push Sensor Data into Database

# Function to save Temperature to DB Table
def conditioner_status_data_handler(json_data: str) -> None:
    """
    Метод для добавления данных кондиционера в соответствующую таблицу в базе данных
    :param json_data: данные кондиционера
    """
    # Parse Data
    json_dict = json.loads(json_data)
    conditioner_id = json_dict['ConditionerID']
    date_and_time = json_dict['Date']
    status = json_dict['Status']
    mode = json_dict['Mode']
    temperature = json_dict['Temperature']

    # Push into DB Table
    db_obj = DatabaseManager()
    db_obj.add_del_update_db_record(
        "insert into CONDITIONER_DATA (ConditionerID, Date_n_Time, Status, Temperature, Mode) values (?,?,?,?,?)",
        [conditioner_id, date_and_time, status, temperature, mode],
    )
    del db_obj
    print("Inserted Temperature Data into Database.")


# ===============================================================
# Master Function to Select DB Funtion based on MQTT Topic


def conditioner_status_handler(topic: str, json_data: str) -> None:
    """
    Метод для обработки поступающих данных от кондиционера
    :param topic:
    :param json_data:
    """
    if topic == "Home/Conditioner/Status":
        conditioner_status_data_handler(json_data)
