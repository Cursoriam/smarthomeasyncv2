from src.subscribers import temperature_sensors_subscribe
from src.subscribers import co2_sensors_subscribe
from src.subscribers import humidity_sensors_subscribe
from src.subscribers import recuperator_subscribe
from src.sqlite import temperature_table_manager
from src.sqlite import humidity_table_manager
from src.sqlite import co2_table_manager
from src.sqlite import db_manager
from src.users import admin


def init_subscriptions() -> None:
    """
    Инициализация подписок на MQTT-брокер
    """
    temperature_sensors_subscribe()
    co2_sensors_subscribe()
    humidity_sensors_subscribe()
    recuperator_subscribe()


def init_db() -> None:
    db_manager.execute_multiple_commands(temperature_table_manager.create_base_command())
    db_manager.execute_multiple_commands(humidity_table_manager.create_base_command())
    db_manager.execute_multiple_commands(co2_table_manager.create_base_command())


def create_admin():
    return admin
