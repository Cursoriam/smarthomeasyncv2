from src.subscribers import temperature_sensors_subscribe
from src.subscribers import co2_sensors_subscribe
from src.subscribers import humidity_sensors_subscribe


def init_subscriptions() -> None:
    """
    Инициализация подписок на MQTT-брокер
    """
    temperature_sensors_subscribe()
    co2_sensors_subscribe()
    humidity_sensors_subscribe()

