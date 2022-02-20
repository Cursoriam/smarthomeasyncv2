from .publisher import publish_data
from src.constants import MQTT_BROKER
from src.constants import MQTT_PORT

topic = "Classroom/Recuperator"


def publish_recuperator_data(msg: str):
    publish_data(MQTT_BROKER, MQTT_PORT, topic, msg)
