# pylint: disable=W0613, C0103
from typing import Any

import paho.mqtt.client as mqttc

from src.sqlite import data_handler

# MQTT Settings
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
KEEP_ALIVE_INTERVAL = 45
MQTT_TOPIC = "Home/#"


def on_connect(client: mqttc, userdata: Any, flags: Any, rc: int) -> None:
    """
    Коллбэк подключения к брокеру
    :param client:
    :param userdata:
    :param flags:
    :param rc:
    """
    if rc == 0:
        print("Connected OK")
        client.subscribe(MQTT_TOPIC)
    else:
        print("Bad connection, RC = ", rc)


# Save Data into DB Table
def on_message(client: mqttc, userdata: Any, msg: mqttc.MQTTMessage) -> None:
    """
    Коллбэк получения сообщения
    :param client:
    :param userdata:
    :param msg:
    """
    # This is the Master Call for saving MQTT Data into DB
    # For details of "sensor_Data_Handler" function please refer "sensor_data_to_db.py"
    print("MQTT Data Received...")
    print("MQTT Topic: " + msg.topic)
    print("Data" + str(msg.payload))
    data_handler(msg.topic, msg.payload)


def assign_callbacks_to_client(client: mqttc) -> None:
    """
    Метод добавления коллбэков клиенту
    :param client:
    """
    client.on_connect = on_connect
    client.on_message = on_message


def broker_subscribe() -> None:
    """
    Метод подписки на топик кондиционера
    """
    sub_client = mqttc.Client(client_id="clientgonnasubA")
    if not sub_client.is_connected():
        sub_client.connect_async(MQTT_BROKER, MQTT_PORT)
        assign_callbacks_to_client(sub_client)
        sub_client.loop_start()
