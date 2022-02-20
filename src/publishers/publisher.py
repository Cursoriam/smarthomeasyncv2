import paho.mqtt.client as mqttc


def on_publish(client, userdata, mid):
    print("Data published")


def publish_data(mqtt_broker: str, mqtt_port: int, topic: str, msg: str):
    client = mqttc.Client(client_id="publisher")
    if not client.is_connected():
        client.connect(mqtt_broker, mqtt_port)
        client.on_publish = on_publish
        client.publish(topic, msg)
        client.disconnect()
