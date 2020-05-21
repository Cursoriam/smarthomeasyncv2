from src.subscribers import broker_subscribe


def init_subscriptions() -> None:
    """
    Инициализация подписок на MQTT-брокер
    """
    broker_subscribe()
