from src.subscribers import temperature_sensors_subscribe
from src.subscribers import heat_sensors_subscribe
from src.subscribers import humidity_sensors_subscribe
from src.subscribers import recuperator_subscribe
from src.sqlite import temperature_table_manager
from src.sqlite import humidity_table_manager
from src.sqlite import heat_table_manager
from src.sqlite import sensors_data_db_manager
from src.sqlite import recuperator_data_db_manager
from src.sqlite import recuperator_schedule_manager
from src.users import admin


def init_subscriptions() -> None:
    """
    Инициализация подписок на MQTT-брокер
    """
    temperature_sensors_subscribe()
    heat_sensors_subscribe()
    humidity_sensors_subscribe()
    recuperator_subscribe()


def init_db() -> None:
    sensors_data_db_manager.execute_multiple_commands(temperature_table_manager.create_base_command())
    sensors_data_db_manager.execute_multiple_commands(humidity_table_manager.create_base_command())
    sensors_data_db_manager.execute_multiple_commands(heat_table_manager.create_base_command())

    recuperator_data_db_manager.execute_multiple_commands(recuperator_schedule_manager.create_base_command())


def create_admin():
    return admin
