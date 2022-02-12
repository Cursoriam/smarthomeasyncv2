from dataclasses import dataclass


# MQTT Settings
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
KEEP_ALIVE_INTERVAL = 45

# Database params
DB_NAME = "SensorsData.db"


class TableManager:
    name: str
    params: str
    insertion_params: str
    insert_db_command: str

    def __init__(self, name, params, insert_db_command):
        self.name = name
        self.params = params
        self.insert_db_command = insert_db_command

    def create_base_schema(self):
        return """
            drop table if exists""" + self.name + """;
            create table if not exists""" + self.name + """ (
            id integer primary key autoincrement,
            Date_n_Time text,
            SensorId text,
            """ + self.params

    def create_insert_command(self):
        return "insert into " + self.name + " " + self.insertion_params + " values (?,?,?,?,?)" # заменить на
        # гененрирование кол-ва вопросов относительно кол-ва параметров и избавиться от insertion_params

temperature_table = TableManager(name="TEMPERATURE_DATA", params="Temperature integer );",
                                 insert_db_command=)
humidity_table = TableManager(name="HUMIDITY_DATA", params="Quantity real );", insert_db_command=)
co2_table = TableManager(name="CO2_DATA", params="Quantity real );", insert_db_command=)
