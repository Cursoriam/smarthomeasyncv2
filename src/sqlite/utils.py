from typing import List, Callable, Dict, Tuple

from src.constants import QUANTITY_OF_BASE_ELEMENTS
from .db_managers import DBManager


class TableManager:
    name: str
    params: List[Dict[str, str]]
    data_parser: Callable
    insert_command: str
    extract_all_command: str

    def __init__(self, name, params, data_parser):
        self.name = name
        self.params = params
        self.data_parser = data_parser
        self.insert_command = self.create_insert_command()
        self.extract_all_command = self.create_extract_all_command()

    def create_base_command(self):
        pass

    def create_insert_command(self) -> str:
        pass

    def extract_command(self, sensor_id: str, limit: int):
        pass

    def create_extract_all_command(self) -> str:
        pass

    def create_delete_command(self) -> str:
        pass


class SqliteSensorsTableManager(TableManager):
    name: str
    params: List[Dict[str, str]]
    data_parser: Callable
    insert_command: str
    extract_all_command: str

    def __init__(self, name, params, data_parser):
        super().__init__(name, params, data_parser)

    def create_base_command(self):
        return """
            drop table if exists """ + self.name + """;
            create table if not exists """ + self.name + """ (
            id integer primary key autoincrement,
            Date_n_Time text,
            SensorId text,
            """ + ', '.join([f'{param["name"]} {param["type"]}' for param in self.params]) + " );"

    def create_insert_command(self):
        return "INSERT INTO " + self.name + "(Date_n_Time, SensorId, " + \
               ', '.join([f'{param["name"]}' for param in self.params]) + ") " +\
               "VALUES(" + ','.join(['?' for i in range(QUANTITY_OF_BASE_ELEMENTS+len(self.params))]) + ")"

    def extract_command(self, sensor_id: str, limit: int):
        return "SELECT * FROM " + self.name + " WHERE SensorId=" + sensor_id + " ORDER BY Date_n_Time DESC LIMIT " + \
               str(limit)

    def create_extract_all_command(self):
        return "SELECT * FROM " + self.name

    def create_delete_command(self) -> str:
        return "SELECT * FROM " + self.name


class SqliteRecuperatorTableManager(TableManager):
    def __init__(self, name, params, data_parser):
        super().__init__(name, params, data_parser)

    def create_base_command(self):
        return """
            drop table if exists """ + self.name + """;
            create table if not exists """ + self.name + """(
            id integer primary key autoincrement,
            Start_Time text,
            End_Time text,
            Temperature integer
            );
        """

    def create_insert_command(self):
        return "INSERT INTO " + self.name + "(Start_Time, End_Time, Temperature) VALUES(?,?,?)"

    def create_extract_all_command(self):
        return "SELECT * FROM " + self.name

    def create_delete_command(self):
        return "DELETE FROM " + self.name + " WHERE rowid=?"


def handle_inserted_data(json_data: str, table_manager: SqliteSensorsTableManager, db_manager: DBManager):
    prepared_data = table_manager.data_parser(json_data)
    try:
        db_manager.execute_single_command(table_manager.create_insert_command(),
                                          [prepared_data[key] for key in prepared_data])
    except Exception as err:
        print(str(err))


def handle_extracted_data(table_manager: TableManager, handled_data: list):
    records_data = [{'date_n_time': data[1], 'sensor_id': data[2]} for data in handled_data]
    i = 0
    for data in records_data:
        data.update({param["name"]: record for param in table_manager.params for record in handled_data[i][3:]})
        i += 1
    return records_data
