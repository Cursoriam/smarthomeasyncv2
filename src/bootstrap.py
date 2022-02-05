from src.subscribers import temperature_sensors_subscribe
from src.subscribers import co2_sensors_subscribe
from src.subscribers import humidity_sensors_subscribe
from src.sqlite import TEMPERATURE_TABLE_SCHEMA
from src.sqlite import HUMIDITY_TABLE_SCHEMA
from src.sqlite import CO2_TABLE_SCHEMA
from src.sqlite import create_table


def init_subscriptions() -> None:
    """
    Инициализация подписок на MQTT-брокер
    """
    temperature_sensors_subscribe()
    co2_sensors_subscribe()
    humidity_sensors_subscribe()


def init_db_dqlite() -> None:
    create_table(TEMPERATURE_TABLE_SCHEMA)
    create_table(HUMIDITY_TABLE_SCHEMA)
    create_table(CO2_TABLE_SCHEMA)

