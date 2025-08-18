import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, on_connect, on_message, broker="mosquitto", port=1883):
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.connect(broker, port)
        self.client.loop_forever()
    def subscribe(self, topic):
        self.client.subscribe(topic)
    def publish(self, topic, message):
        self.client.publish(topic, message)