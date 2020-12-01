import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

mqtt_host = "farmer.cloudmqtt.com"
mqtt_port = 34511
mqtt_user = "itiwppsz"
mqtt_password = "BkRYsnNyy_tk"

client.connect("farmer.cloudmqtt.com", 34511, 60)


client.loop_forever()