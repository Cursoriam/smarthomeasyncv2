from src.subscribers import broker_subscribe
from src.constants import MQTT_BROKER
from src.constants import MQTT_PORT

userdata = {"mqtt_topic": "Classroom/CO2_Sensors"}


def co2_sensors_subscribe():
    broker_subscribe(MQTT_BROKER, MQTT_PORT, "co2_sensors_client", userdata)
