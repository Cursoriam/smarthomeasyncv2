from src.subscribers import conditioner_subscribe


def init_subscriptions() -> None:
    """
    Инициализация подписок на MQTT-брокер
    """
    conditioner_subscribe()
