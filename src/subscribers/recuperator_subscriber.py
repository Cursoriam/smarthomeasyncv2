from src.subscribers import broker_subscribe
from src.constants import MQTT_BROKER
from src.constants import MQTT_PORT
from .subscriber import on_message_default

userdata = {"mqtt_topic": "Classroom/Recuperator", }


def recuperator_subscribe():
    broker_subscribe(MQTT_BROKER, MQTT_PORT, "recuperator_client", userdata, on_message_default)
