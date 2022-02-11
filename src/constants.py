# MQTT Settings

MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
KEEP_ALIVE_INTERVAL = 45

# Database params

DB_NAME = "SensorsData.db"
BASE_TABLE_SCHEMA = """
drop table if exists TEMPERATURE_DATA ;
create table if not exists TEMPERATURE_DATA (
    id integer primary key autoincrement,
    Date_n_Time text,
    SensorId text,
"""
TEMPERATURE_TABLE_PARAMS = """
Temperaure integer
"""
HUMIDITY_TABLE_PARAMS = """
Quantity real
"""
CO2_TABLE_PARAMS = """
Quantity real
"""
