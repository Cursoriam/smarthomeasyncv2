from src.subscribers import temperature_sensors_subscribe
from src.subscribers import co2_sensors_subscribe
from src.subscribers import humidity_sensors_subscribe
from src.sqlite import create_table
from src.sqlite import TemperatureSchema
from src.sqlite import HumiditySchema
from src.sqlite import C02Schema


def init_subscriptions() -> None:
    """
    Инициализация подписок на MQTT-брокер
    """
    temperature_sensors_subscribe()
    co2_sensors_subscribe()
    humidity_sensors_subscribe()


def init_db_sqlite() -> None:
    create_table(TemperatureSchema.create_schema())
    create_table(HumiditySchema.create_schema())
    create_table(C02Schema.create_schema())

