from typing import Any
from typing import Dict
import random
import threading
import json
from datetime import datetime

import paho.mqtt.client as mqtt

MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
KEEP_ALIVE_INTERVAL = 45
MQTT_TEMPERATURE_TOPIC = "Classroom/Temperature_Sensors"
MQTT_HUMIDITY_TOPIC = "Classroom/Humidity_Sensors"
MQTT_HEAT_TOPIC = "Classroom/Heat_Sensors"

MODES = ['Easy', 'Normal', 'Hard']


def on_connect(mqttc: mqtt, userdata: Any, flags: Any, rc: int):
    if rc != 0:
        pass
        print("Unable to connect to MQTT Broker...")
    else:
        print("Connected with MQTT Broker: " + str(MQTT_BROKER))


def on_disconnect(mqttc: mqtt, userdata: Any, flags: Any, rc: int):
    if rc != 0:
        pass
        print("Unable to disconnect to MQTT Broker...")
    else:
        print("Disconnected from MQTT Broker: " + str(MQTT_BROKER))


mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.connect_async(MQTT_BROKER, int(MQTT_PORT), int(KEEP_ALIVE_INTERVAL))
mqttc.loop_start()


def publish_to_topic(topic, message):
    mqttc.publish(topic, message)
    print("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))


def prepare_data_to_publish(additional_data: Dict):
    data = {'Date_n_Time': (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f"),
            'SensorId': str(random.randrange(1, 3))}
    data.update(additional_data)
    return json.dumps(data)


toggle = 0


def publish_fake_sensor_values_to_mqtt():
    threading.Timer(3.0, publish_fake_sensor_values_to_mqtt).start()
    global toggle
    if toggle == 0:
        print("Publishing fake Temperature Value")
        publish_to_topic(MQTT_TEMPERATURE_TOPIC, prepare_data_to_publish({"Temperature": random.randrange(15, 30)}))
        toggle = random.randrange(1, 3)
    elif toggle == 1:
        print("Publishing fake humidity Value")
        publish_to_topic(MQTT_HUMIDITY_TOPIC, prepare_data_to_publish({"Quantity": random.randrange(40, 70)}))
        toggle = random.choice([0, 2])
    elif toggle == 2:
        print("Publishing fake heat Value")
        publish_to_topic(MQTT_HEAT_TOPIC, prepare_data_to_publish({"Quantity": random.randint(0,
                                                                   int((2.0 - 0.3) / 0.1)) * 0.1 + 0.3}))
        toggle = random.randrange(0, 2)


publish_fake_sensor_values_to_mqtt()
