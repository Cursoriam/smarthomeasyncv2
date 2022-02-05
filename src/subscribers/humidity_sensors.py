from src.subscribers import broker_subscribe
from src.constants import MQTT_BROKER
from src.constants import MQTT_PORT

userdata = {"mqtt_topic": "Classroom/Humidity_Sensors"}


def humidity_sensors_subscribe():
    broker_subscribe(MQTT_BROKER, MQTT_PORT, "humidity_sensors_client", userdata)
