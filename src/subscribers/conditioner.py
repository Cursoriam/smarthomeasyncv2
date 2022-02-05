from src.subscribers import broker_subscribe
from src.constants import MQTT_BROKER
from src.constants import MQTT_PORT

MQTT_TOPIC = "Home/Conditioner"

userdata = {"mqtt_topic": MQTT_TOPIC}


def conditioner_subscribe():
    broker_subscribe(MQTT_BROKER, MQTT_PORT, "conditioner_client", userdata)
