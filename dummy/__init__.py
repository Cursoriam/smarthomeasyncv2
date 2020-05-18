import paho.mqtt.client as mqtt
import random, threading, json
from datetime import datetime

# ====================================================
# MQTT Settings
MQTT_Broker = "test.mosquitto.org"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "Home/Conditioner/Status"


# ====================================================

def on_connect(mqttc, userdata, flags, rc):
    if rc != 0:
        pass
        print("Unable to connect to MQTT Broker...")
    else:
        print("Connected with MQTT Broker: " + str(MQTT_Broker))


def on_disconnect(mqttc, userdata, flags, rc):
    if rc != 0:
        pass


mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.connect_async(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
mqttc.loop_start()


def publish_To_Topic(topic, message):
    mqttc.publish(topic, message)
    print("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))

# ====================================================
# FAKE SENSOR
# Dummy code used as Fake Sensor to publish some random values
# to MQTT Broker


toggle = 0


def publish_Fake_Sensor_Values_to_MQTT():
    threading.Timer(3.0, publish_Fake_Sensor_Values_to_MQTT).start()
    global toggle
    if toggle == 0:
        Humidity_Fake_Value = float("{0:.2f}".format(random.uniform(50, 100)))

        Humidity_Data = {'ConditionerID': "Dummy-1", 'Date': (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f"),
                         'Status': Humidity_Fake_Value}
        humidity_json_data = json.dumps(Humidity_Data)

        print("Publishing fake Humidity Value: " + str(Humidity_Fake_Value) + "...")
        publish_To_Topic(MQTT_Topic, humidity_json_data)


publish_Fake_Sensor_Values_to_MQTT()
